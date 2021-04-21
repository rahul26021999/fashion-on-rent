import stripe 

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .cart import Cart
from .forms import CheckoutForm

from apps.order.utilities import checkout, notify_customer, notify_vendor
from django.contrib.auth.decorators import login_required


def show_cart(request):
    form = CheckoutForm()
    return render(request, 'cart/cart.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY})

def cart_remove(request):
    id=request.GET.get("id",'')
    cart = Cart(request)
    cart.remove(product_id=id)
    return redirect('cart')



@login_required
def cart_detail(request):
    cart = Cart(request)
    
    form = CheckoutForm(request.POST)
    if form.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe_token = form.cleaned_data['stripe_token']

        try:
            charge = stripe.Charge.create(
                amount=int(cart.get_total_cost() * 100),
                currency='USD',
                description='Charge from Fashion On Rent',
                source=stripe_token
            )

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            place = form.cleaned_data['place']

            order = checkout(request, first_name, last_name, email, address, zipcode, place, phone, cart.get_total_cost())

            cart.clear()

            # notify_customer(order)
            # notify_vendor(order)

            return redirect('success')
        
        except Exception:
            messages.error(request, 'There was something wrong with the payment')
    

def success(request):
    return render(request, 'cart/success.html')
from apps.product.models import Category
from apps.product.models import Tags


def menu_categories(request):
    categories = Category.objects.all()
    return {'menu_categories': categories}

def menu_tags(request):
    tags = Tags.objects.all()
    return {'menu_tags': tags}
# Generated by Django 3.2 on 2021-04-21 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('order', '0002_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.RemoveField(
            model_name='order',
            name='vendors',
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='vendor.vendor'),
            preserve_default=False,
        ),
    ]

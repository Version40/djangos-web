# Generated by Django 4.2.3 on 2023-07-11 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_order_pizza_order_is_paid_order_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='orderitems',
            options={'verbose_name': 'Елементи замовлень', 'verbose_name_plural': 'Елементи замовлень'},
        ),
    ]

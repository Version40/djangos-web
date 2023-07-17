# Generated by Django 4.2.3 on 2023-07-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_orderitems_pizza_orderitems_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='pizza',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='pizza',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.pizza'),
        ),
    ]

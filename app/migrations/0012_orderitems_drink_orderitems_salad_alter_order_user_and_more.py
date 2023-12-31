# Generated by Django 4.2.3 on 2023-07-12 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='drink',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.drink'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='salad',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.salad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='pizza',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.pizza'),
        ),
    ]

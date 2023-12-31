# Generated by Django 4.2.3 on 2023-07-09 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pizza_compaund'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('salad_name', models.CharField(max_length=100, verbose_name='Назва салату')),
                ('compaund', models.CharField(default=0, max_length=150, verbose_name='Склад салату')),
                ('price', models.IntegerField(default=100, verbose_name='Ціна')),
                ('weight', models.IntegerField(default=20, verbose_name='Вага')),
                ('images', models.ImageField(upload_to='salad', verbose_name='Фото піци')),
            ],
            options={
                'verbose_name': 'Салат',
                'verbose_name_plural': 'Салати',
            },
        ),
    ]

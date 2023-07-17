from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

import uuid
from PIL import Image


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ImageCarousel(BaseModel):
    title = models.CharField('Назва новинки', max_length=100)
    images = models.ImageField(upload_to='app')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class PizzaCategory(BaseModel):
    category_name = models.CharField('Назва категорії', max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Pizza(BaseModel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField('Назва піци', max_length=100)
    compaund = models.CharField('Склад піци', max_length=150)
    weight = models.IntegerField('Вага', default=100)
    price = models.IntegerField('Ціна', default=100)
    images = models.ImageField('Фото піци', upload_to='pizza')

    def __str__(self):
        return self.pizza_name

    class Meta:
        verbose_name = 'Піца'
        verbose_name_plural = 'Піца'


class Salad(BaseModel):
    salad_name = models.CharField('Назва салату', max_length=100)
    compaund = models.CharField('Склад салату', max_length=150, default=0)
    price = models.IntegerField('Ціна')
    weight = models.IntegerField('Вага')
    images = models.ImageField('Фото салату', upload_to='salad')

    def __str__(self):
        return self.salad_name

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салати'


class Drink(BaseModel):
    drink_name = models.CharField('Назва напою', max_length=100)
    price = models.IntegerField('Ціна')
    weight = models.IntegerField('Вага')
    images = models.ImageField('Фото напою', upload_to='drink')

    def __str__(self):
        return self.drink_name

    class Meta:
        verbose_name = 'Напій'
        verbose_name_plural = 'Напої'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Ім'я та Прізвище", max_length=50, default='UnknowUser')
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    phone_number = models.IntegerField('Номер телефону', default=0)
    city = models.CharField('Місто', max_length=12, default='Київ')
    address = models.CharField('Адреса', max_length=40, default='Невідомо')
    apartment = models.IntegerField('Номер квартири', default='1111')

    def __str__(self):
        return f'Профайл користувача {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайли'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    item_count = models.IntegerField(default=0)

    def update_totals(self):
        order_items = self.order_items.all()
        self.total_price = sum(
            order_item.get_price() for order_item in order_items
        )
        self.item_count = order_items.count()
        self.save()

    def get_order_total(self):
        order_items = self.order_items.filter(order=self)
        total_price = 0

        for order_item in order_items:
            if order_item.pizza:
                total_price += order_item.pizza.price
            elif order_item.salad:
                total_price += order_item.salad.price
            elif order_item.drink:
                total_price += order_item.drink.price

        return total_price

    def get_order_count(self):
        order_items = self.order_items.all()
        total_count = order_items.count()
        return total_count

    def __str__(self):
        return f'Замовлення {self.uid}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, blank=True)
    salad = models.ForeignKey(Salad, on_delete=models.CASCADE, null=True, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True, blank=True)

    def get_price(self):
        if self.pizza:
            return self.pizza.price
        elif self.salad:
            return self.salad.price
        elif self.drink:
            return self.drink.price
        else:
            return 0

    class Meta:
        verbose_name = 'Замовлення елемента'
        verbose_name_plural = 'Замовлення елементів'

    class Meta:
        verbose_name = 'Замовлення елемента'
        verbose_name_plural = 'Замовлення елементів'
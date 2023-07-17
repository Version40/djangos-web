from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import auth
from django.contrib import messages

from app.models import *
from app.forms import *


class Home(View):
    model1 = ImageCarousel
    model2 = Pizza
    model3 = Salad
    model4 = Drink
    model5 = Order
    template = 'main.html'

    def get_context_data(self):
        order = None
        if self.request.user.is_authenticated:
            order, _ = self.model5.objects.get_or_create(user=self.request.user, is_paid=False)
        else:
            order, _ = self.model5.objects.get_or_create(user=None, is_paid=False)

        context = {
            'carousel': self.model1.objects.all(),
            'pizzas': self.model2.objects.all(),
            'salad': self.model3.objects.all(),
            'drink': self.model4.objects.all(),
            'order': order,
            'form_login': LoginForm(),
            'form_register': UserRegistrationForm(),
            'selected_category': self.request.GET.get('category'),
            'order_total_price': order.total_price if order else 0,
            'order_item_count': order.item_count if order else 0,
        }
        return context

    def get(self, request, *args, **kwargs):
        valid_categories = ["М'ясні", 'Вегетеріанські', 'Гриль', 'Гострі']
        sort = request.GET.get('sort')
        category = request.GET.get('category')

        pizzas = self.model2.objects.all()

        if category and category in valid_categories:
            pizzas = pizzas.filter(category__category_name=category)

        if sort == 'asc':
            pizzas = pizzas.order_by('price')
        elif sort == 'desc':
            pizzas = pizzas.order_by('-price')

        context = self.get_context_data()
        context['pizzas'] = pizzas
        context['selected_category'] = category

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        if request.POST.get('login') == 'login':
            form_login = LoginForm(request.POST)
            if form_login.is_valid():
                cd = form_login.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/')

                context = self.get_context_data()
                context['form_login'] = form_login
                return render(request, self.template, context)
            else:
                context = self.get_context_data()
                context['form_login'] = form_login
                return render(request, self.template, context)

        elif request.POST.get('register') == 'register':
            form_register = UserRegistrationForm(request.POST)
            if form_register.is_valid():
                new_user = form_register.save()
                new_user.set_password(form_register.cleaned_data['password'])
                new_user.save()
                user = authenticate(username=new_user.username, password=form_register.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')

            context = self.get_context_data()
            context['form_register'] = form_register
            return render(request, self.template, context)

        context = self.get_context_data()
        context['form_login'] = LoginForm()
        context['form_register'] = UserRegistrationForm()
        return render(request, self.template, context)


def logout(request):
    url_from = request.META['HTTP_REFERER']
    auth.logout(request)
    return redirect(url_from)


class AddOrderItemView(View):
    @staticmethod
    def get(request, item_type, item_uid):
        try:
            if request.user.is_authenticated:
                order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)
            else:
                order, _ = Order.objects.get_or_create(user=None, is_paid=False)

            if item_type == 'pizza':
                item_obj = Pizza.objects.get(uid=item_uid)
                order_item = OrderItem.objects.create(order=order, pizza=item_obj)
            elif item_type == 'salad':
                item_obj = Salad.objects.get(uid=item_uid)
                order_item = OrderItem.objects.create(order=order, salad=item_obj)
            elif item_type == 'drink':
                item_obj = Drink.objects.get(uid=item_uid)
                order_item = OrderItem.objects.create(order=order, drink=item_obj)
            else:
                return redirect('/')

            # Оновлення підсумків замовлення
            order.update_totals()

            return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/')


def order(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(is_paid=False, user=request.user).first()
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, instance=profile)
    else:
        order = Order.objects.filter(is_paid=False, user=None).first()
        form = ProfileForm(request.POST or None)

    if order is None:
        order = Order.objects.create(is_paid=False, user=request.user if request.user.is_authenticated else None)

    if request.method == 'POST' and form.is_valid():
        form.save()

    context = {
        'order': order,
        'order_total_price': order.total_price if order else 0,
        'order_item_count': order.item_count if order else 0,
        'form_login': LoginForm(),
        'form_register': UserRegistrationForm(),
        'form': form,
    }
    return render(request, 'order.html', context)


class RemoveOrderItemsView(View):
    @staticmethod
    def get(request, item_type, uid):
        try:
            if item_type == 'pizza':
                OrderItem.objects.filter(pizza__isnull=False, pizza__uid=uid).delete()
            elif item_type == 'salad':
                OrderItem.objects.filter(salad__isnull=False, salad__uid=uid).delete()
            elif item_type == 'drink':
                OrderItem.objects.filter(drink__isnull=False, drink__uid=uid).delete()
            else:
                return redirect('')

            order = Order.objects.get(user=request.user if request.user.is_authenticated else None, is_paid=False)

            order.update_totals()

            return redirect('/order/')
        except Exception as e:
            print(e)
            return redirect('/error/')


def success(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(is_paid=False, user=request.user).first()
    else:
        order = Order.objects.filter(is_paid=False, user=None).first()

    if order is not None:
        order.is_paid = True
        order.save()
        messages.success(request, "Дякуємо за замовлення!<br>Незабаром з Вами зв'яжуться для підтвердження замовлення.")

    return redirect('home')

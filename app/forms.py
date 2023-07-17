import re
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_auth', 'id': 'login', 'placeholder': 'Ваш логін'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form_auth', 'id': 'pass', 'placeholder': 'Ваш поточний пароль'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user_exists = User.objects.filter(username=username).exists()
            if not user_exists:
                raise forms.ValidationError('Користувач з таким ім\'ям не існує')
            else:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError('Невірний пароль')

        return cleaned_data


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_reg', 'placeholder': 'Логін'})
    )
    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_reg_flex', 'placeholder': "Ваше ім'я"})
    )
    last_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_reg_flex', 'placeholder': 'Ваше прізвище'})
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_reg', 'placeholder': 'Email'})
    )
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'class': 'form_reg_flex', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'class': 'form_reg_flex', 'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = str(cleaned_data.get('email'))
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Користувач з таким ім\'ям уже існує')

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError('Введіть дійсну адресу електронної пошти')

        if password and password2 and password != password2:
            raise forms.ValidationError('Паролі не співпадають')

        return cleaned_data

    def save(self, commit=False):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        return user


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        label="Ім'я та Прізвище",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_contact', 'placeholder': "Ім'я та Прізвище"})
    )
    phone_number = forms.CharField(
        label="Номер телефону",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_contact', 'placeholder': "Номер телефону"})
    )
    city = forms.CharField(
        label="Місто",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_contact', 'placeholder': "Місто"})
    )
    address = forms.CharField(
        label="Вулиця",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_contact', 'placeholder': "Вулиця"})
    )
    apartment = forms.CharField(
        label="Номер квартири",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form_contact', 'placeholder': "Номер квартири"})
    )

    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'city', 'address', 'apartment']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введіть Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть Email'})
    )
    username = forms.CharField(
        label='Введіть логін',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть логін'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузити фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
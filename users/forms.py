from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.template.defaultfilters import first

from users.models import User

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label = 'Name',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                            'class':'form-control',
    #                            'placeholder': 'Введите ваше имя пользователя',})
    # )
    # password = forms.CharField(
    #     label = 'Password',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class':'form-control',
    #                                       'placeholder': 'Введите ваш пароль'}),
    # )


class UserRegistrartion(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите вашу фамилию",
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше email *youremail@example.com",
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваш пароль"
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "подтвердите ваш пароль"
    #         }
    #     )
    # )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )
        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
        username = forms.CharField()
        email = forms.CharField()

    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": "form-control mt-3 "}), required=False
    # )
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите вашу фамилию",
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs ={
    #             "class": "form-control",
    #             "place_holder": "Ведите ваше email *youremail@example.com",})
    #             )

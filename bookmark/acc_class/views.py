from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django import forms


class AccLogin(LoginView):
    # ссылка на наш шаблон
    template_name = 'acc_class/login.html'

    # метод создания формы
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(AccLogin, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Login'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        return form

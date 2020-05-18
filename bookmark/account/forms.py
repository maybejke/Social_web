from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    passwords = forms.CharField(widget=forms.PasswordInput)

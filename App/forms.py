from django import forms


class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignIn(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

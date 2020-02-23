from django import forms
from . models import Driver, User


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ('driver', 'age', 'vehicle')


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

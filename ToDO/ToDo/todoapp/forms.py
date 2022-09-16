from django import forms
from django.contrib.auth.models import User
from todoapp.models import Todos


# class RegistrationForm(forms.Form):
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     username=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
        widgets={
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
        }

class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['task_name']
        widgets={"task_name":forms.TextInput(attrs={"class":"form-control"})}

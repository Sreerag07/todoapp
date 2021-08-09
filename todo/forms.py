from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Completed,Todo
from django.forms import ModelForm
# registration form
class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields="__all__"

        widgets={
            "created_by":forms.TextInput(attrs={'class':"form-control"}),
            "completed": forms.Select(attrs={'class': "form-select"}),
            "task": forms.TextInput(attrs={'class': "form-control"}),
        }
class BrandCreationForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets = {
                   "brand_name":forms.TextInput(attrs={"class":"form-control"})
        }



class RegistrationForm(UserCreationForm):
    # to style fields from UserCreationForm()
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

        # to style fields from User() model
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }
class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"

        widgets={
            "mobile_name":forms.TextInput(attrs={'class':"form-control"}),
            "brand": forms.Select(attrs={'class': "form-select"}),
            "price": forms.TextInput(attrs={'class': "form-control"}),
            "memory": forms.TextInput(attrs={'class': "form-control"}),
            "os": forms.TextInput(attrs={'class': "form-control"}),
            "specs": forms.TextInput(attrs={'class': "form-control"}),
            "image": forms.FileInput(attrs={'class': "form-control"}),
        }
class BrandCreationForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets = {
                   "brand_name":forms.TextInput(attrs={"class":"form-control"})
        }

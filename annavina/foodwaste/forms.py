from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import foodmart

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_customer')

class FoodmartForm(forms.ModelForm):
    class Meta:
        model = foodmart
        fields = ['name', 'description', 'pincode','address','phone_number','quantity']


class SearchFoodMartForm(forms.Form):
    pincode = forms.CharField(label='Pincode', max_length=6)
    distance = forms.DecimalField(label='Distance (in kilometers)', max_digits=5, decimal_places=2)

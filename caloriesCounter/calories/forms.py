from django.forms import ModelForm
from .models import *
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class fooditemForm(ModelForm):
    class Meta:
        model=FoodItems
        fields="__all__"

class UserFoodForm(ModelForm):
    class Meta:
        model=consume
        fields="__all__"

# class FoodSelectForm(forms.Form):
#     food = forms.ModelMultipleChoiceField(queryset=FoodItems.objects.all(), label="Select Food")

# class createUserForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

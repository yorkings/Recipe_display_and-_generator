from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

from .models import *

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'abc@gmail.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("The username is already taken. Please enter a different username.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("The email is already taken. Please enter a different email.")
        return email


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password=forms.CharField(min_length=4,widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author','slug']  # Use a list or tuple, and use the correct field name

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'     

class ProfileForm(forms.ModelForm):
    mobile_no = PhoneNumberField(region="KE")
    class Meta:
        model = Profile
        fields = ['bios', 'image', 'location', 'mobile_no']
        widgets = {
            'bios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
             'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+254 ------'}),
        }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }

class CosmeticsForm(forms.ModelForm):
    class Meta:
        model=Cosmetics
        fields="__all__"

class LearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = ['image', 'video', 'ingredients', 'procedure', 'difficulty']
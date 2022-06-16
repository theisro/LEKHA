from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OnboardingForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=200)
    last_name = forms.CharField(label="Last name", max_length=200)
    aword1 = forms.CharField(label="Artist word 1", max_length=200)
    aword2 = forms.CharField(label="Artist word 2", max_length=200)
    aword3 = forms.CharField(label="Artist word 3", max_length=200)
    bio = forms.CharField(label="biography", max_length=200)
    insta_handle = forms.CharField(label="insta handle", max_length=200)
    fb_handle = forms.CharField(label="fb handle", max_length=200)
    twitter_handle = forms.CharField(label="twitter handle", max_length=200)
    private = forms.BooleanField(label="private")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

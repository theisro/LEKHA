from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## Forms.py in django is used to house forms that are used on the websites. Django automatically generates html code for forms based on a blueprint
## defined here, and creates an input field for each of the variables defined in the classes here. That way, if you want to change the form on the frontend,
## you only need to change this file (and the views file to deal with the POST request) and everything else is automatically updated.

class OnboardingForm(forms.Form):
    '''
    Form for user onboarding, which collects all the relevant info. 
    '''
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
    '''
    Extension of the base user registration form provided by django.
    Adds the email field as an input.
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

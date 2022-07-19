from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Forms.py in django is used to house forms that are used on the websites. Django automatically generates html code for forms based on a blueprint
# defined here, and creates an input field for each of the variables defined in the classes here. That way, if you want to change the form on the frontend,
# you only need to change this file (and the views file to deal with the POST request) and everything else is automatically updated.




class OnboardingForm(forms.Form):
    '''
    Form for user onboarding, which collects all the relevant info. 
    '''
    first_name = forms.CharField(label="First name", max_length=200, widget=forms.TextInput(attrs={
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    last_name = forms.CharField(label="Last name", max_length=200, widget=forms.TextInput(attrs={
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    aword1 = forms.CharField(label="Artist word 1", max_length=200, widget=forms.TextInput(attrs={
                             'placeholder': 'eg: painter', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    aword2 = forms.CharField(label="Artist word 2", max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'eg: filmmaker', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    aword3 = forms.CharField(label="Artist word 3", max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'eg: designer', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    bio = forms.CharField(label="Biography (optional)", required=False, max_length=1200, widget=forms.Textarea(attrs={
        'class': 'appearance-none resize-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    insta_handle = forms.CharField(label="Insta handle", required=False, max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Instagram', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    fb_handle = forms.CharField(label="Fb handle", required=False, max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Facebook', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    twitter_handle = forms.CharField(label="Twitter handle", required=False, max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Twitter', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    profile_image = forms.FileField(label="Archive Image", required=False)
    cv = forms.FileField(label="Archive Image", required=False)
    # private = forms.BooleanField(label="Private", required=False)


class UserRegisterForm(UserCreationForm):
    '''
    Extension of the base user registration form provided by django.
    Adds the email field as an input.
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'appearance-none my-0 rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}),
            'email': forms.EmailInput(attrs={'class': 'appearance-none my-0 rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}),
            'password1': forms.PasswordInput(attrs={'class': 'appearance-none my-0 rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}),
            'password2': forms.PasswordInput(attrs={'class': 'appearance-none my-0 rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}),
        }


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}
    )
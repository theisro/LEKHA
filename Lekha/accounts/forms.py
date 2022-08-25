from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from archival.models import Archive

# Forms.py in django is used to house forms that are used on the websites. Django automatically generates html code for forms based on a blueprint
# defined here, and creates an input field for each of the variables defined in the classes here. That way, if you want to change the form on the frontend,
# you only need to change this file (and the views file to deal with the POST request) and everything else is automatically updated.
        
class OnboardingForm(forms.Form):
    '''
    Form for user onboarding, which collects all the relevant info. 

    Redundant if we use the ModelForm variant. 
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
    archive_image = forms.ImageField(label="Archive Image", required=False, help_text='max 42 megabytes') ## change helptext
    cv = forms.FileField(label="CV", required=False, help_text='max 42 megabytes')
    private = forms.BooleanField(label="Private", required=False)
    archive_type = forms.ChoiceField(label="Archive Type", choices=[('Artist', 'Artist'), ('Institution', 'Institution'), ('Collector', 'Collector')], required=True)
    archive_name = forms.SlugField(label="Archive Name", max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'unique archive name', 'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))



class UserRegisterForm(UserCreationForm):
    '''
    Extension of the base user registration form provided by django.
    Adds the email field as an input.
    '''
    username = forms.SlugField(widget=forms.TextInput(attrs={
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

class AccountSettingsFormUser(forms.ModelForm):
    username = forms.SlugField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(AccountSettingsFormUser, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class AccountSettingsFormArtistArchive(forms.ModelForm):
    archive_slug = forms.SlugField(label="Archive Name", max_length=200)
    archive_image = forms.ImageField(label="Archive Image", required=False, help_text='max 42 megabytes', ) ## change helptext
    cv = forms.FileField(label="CV", required=False, help_text='max 42 megabytes')
    bio = forms.CharField(label="Bio", max_length=200)
    fb_link = forms.CharField(label="Facebook link", max_length=200)
    insta_link = forms.CharField(label="Instagram link", max_length=200)
    twitter_link = forms.CharField(label="Twitter link", max_length=200)


    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)
    aword1 = forms.CharField(label="Aword 1", max_length=200)
    aword2 = forms.CharField(label="Aword 2", max_length=200)
    aword3 = forms.CharField(label="Aword 3", max_length=200)

    class Meta():
        model = Archive
        fields = ('archive_slug', 
                  'archive_image', 
                  'cv', 
                  'bio', 
                  'fb_link', 
                  'insta_link', 
                  'twitter_link',  
                  'first_name', 
                  'last_name', 
                  'aword1', 
                  'aword2', 
                  'aword3')
    


class AccountSettingsFormInstitutionalArchive(forms.ModelForm):
    archive_slug = forms.SlugField(label="Archive Name", max_length=200)
    archive_image = forms.ImageField(label="Archive Image", required=False, help_text='max 42 megabytes', ) ## change helptext
    cv = forms.FileField(label="CV", required=False, help_text='max 42 megabytes')
    bio = forms.CharField(label="Bio", max_length=200)
    fb_link = forms.CharField(label="Facebook link", max_length=200)
    insta_link = forms.CharField(label="Instagram link", max_length=200)
    twitter_link = forms.CharField(label="Twitter link", max_length=200)

    institution_name = forms.CharField(max_length=50)
    institution_website = forms.URLField(required=False)

    class Meta():
        model = Archive
        fields = ('archive_slug', 
                  'archive_image', 
                  'cv', 
                  'bio', 
                  'fb_link', 
                  'insta_link', 
                  'twitter_link', 
                  'institution_name', 
                  'institution_website')



class AccountSettingsFormPrivacy(forms.ModelForm):
    private = forms.BooleanField(label="Private", required=False)

    class Meta():
        model = Archive
        fields = ('private',)


class AccountSettingsFormContact(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)



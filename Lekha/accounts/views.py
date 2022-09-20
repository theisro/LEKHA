from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import OnboardingForm, UserRegisterForm, AccountSettingsFormUser, AccountSettingsFormArtistArchive, AccountSettingsFormInstitutionalArchive, AccountSettingsFormPrivacy, AccountSettingsFormContact
from archival.models import Archive, Folder

from django.contrib.auth.views import LoginView    

from django.contrib.auth import logout

from django.core.files.storage import FileSystemStorage

from archival.models import Archive

import secrets #for generating random slugs (for now, remove when redundant)

# decorator to enforce that users need to be logged in to access some pages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def onboarding(response):
    if response.method == "POST":
        # if the form has been submitted
        # Serve the form -> response.POST
        form = OnboardingForm(response.POST, response.FILES)

        if form.is_valid(): # if the all the fields on the form pass validation

            ### these variables need to be dynamically assigned and/or properly retrieved from the html. 
            archive_slug = secrets.token_hex(5) # generates a random 5 character slug --> testing purposes only!!!!!
            private = False ## testing purposes only!!
            archive_type="ARTIST" ## needs to get input from frontend, testing purposes only!!!

            ## save uploaded files to disk. Path of file location is stored in the archive database automatically to reduce the database size.
            fs = FileSystemStorage()
            cv = fs.save(response.FILES['cv'].name, response.FILES['cv'])
            archive_image = fs.save(response.FILES['archive_image'].name, response.FILES['archive_image'])

            # create a new archive with the parameters retrieved from the form. currently logged in user is automatically linked
            archive = Archive(first_name=form.cleaned_data.get("first_name"),
                            last_name=form.cleaned_data.get("last_name"),
                            aword1=form.cleaned_data.get("aword1"),
                            aword2=form.cleaned_data.get("aword2"),
                            aword3=form.cleaned_data.get("aword3"),
                            bio=form.cleaned_data.get("bio"),
                            insta_link=form.cleaned_data.get("insta_link"),
                            fb_link=form.cleaned_data.get("fb_link"),
                            twitter_link=form.cleaned_data.get("twitter_link"),
                            cv = cv,
                            archive_image = archive_image,

                            private=private,
                            archive_type=archive_type,
                            archive_slug=archive_slug,
                            )

            # save the archive to the database (save also automatically assigns timestamps, and the user to the archive: created, modified, creator)
            archive.save()

            ## step 2 create filesystem and link it to the archive
            media_library = Folder.add_root(name="{}'s media_library".format(archive_slug), archive=archive)
            archive_root = Folder.add_root(name="{}'s archive".format(archive_slug), archive=archive)

            # Redirect to index page
            return redirect('dashboard')

    else:
        # If the form is not submitted (page is loaded for example)
        # -> Serve the empty form
        form = OnboardingForm()

    return render(response, "accounts/onboarding.html", {"form": form})


def register(request):
    if request.method == "POST":
        # if the form is submitted
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # if the inputs are all valid, save the form and create a new user
            form.save()
            # then redirect home
            return redirect('onboarding')
    else:
        form = UserRegisterForm()

    return render(request, "accounts/register.html", {"form": form})

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('index')


@login_required
def account_settings(request):
    '''
    This view is for the user to change their account settings. All possible changes can be made here.

    Forms that change the user's account settings are defined in the forms.py file in the accounts app. 
    Since there are multiple types of archives (Artist, Institution), each of these types have their own form as they have unique fields.
    These forms are passed to the template to render in the "if archive.archive_type == 'ARTIST'" and "if archive.archive_type == 'INSTITUTION'" sections.

    The post request section is also a bit more complicated than usual due to the presence of multiple forms on the same page.
    The code checks which form is submitted everytime a POST request happens, and only binds that form to the request, ensuring 
    that only the form that is submitted is bound to the request.

    Once the form that has been submitted is determined, the form is validated. If the form is valid, the form is saved to the database.

    All fields are prepopulated with their existing values, so the user can see what their current settings are. 
    This is done through the 'initial' argument in the form.

    Finally, this view is bound to only users thar are logged in, through the @login_required decorator.
    '''

    # retrieve the archive object of the current user, so we can edit the corresponding fields of that archive
    archive = Archive.objects.get(creator=request.user)

    if request.method == "POST":
        # if any of the forms are submitted:
        if 'user_settings' in request.POST:
            # if the submitted form is the user settings form
            form1 = AccountSettingsFormUser(request.POST, instance=request.user, initial={'username': request.user.username, 
                                                                        'email': request.user.email
                                                                        })
            if form1.is_valid():
                form1.save()
        else:
            # of the submitted form is not the user settings form (ensures that other forms are kept unbound, ie so they dont get wiped)
            form1 = AccountSettingsFormUser(instance=request.user, initial={'username': request.user.username, 
                                                                        'email': request.user.email
                                                                        })

        if 'archive_settings' in request.POST:
            # if the submitted form is the archive settings form      
            if archive.archive_type == "ARTIST":
                form2 = AccountSettingsFormArtistArchive(request.POST, instance=archive)
            elif archive.archive_type == "INSTITUTION":
                form2 = AccountSettingsFormInstitutionalArchive(request.POST, instance=archive)

            if form2.is_valid():
                form2.save()

        else:
            # if the submitted form is not the archive settings form
            if archive.archive_type == "ARTIST":
                form2 = AccountSettingsFormArtistArchive(instance=archive, initial={
                                                                                    'archive_slug': archive.archive_slug, 
                                                                                    'bio': archive.bio, 
                                                                                    'insta_link': archive.insta_link, 
                                                                                    'fb_link': archive.fb_link, 
                                                                                    'twitter_link':archive.twitter_link, 
                                                                                    'first_name':archive.first_name, 
                                                                                    'last_name':archive.last_name, 
                                                                                    'aword1':archive.aword1, 
                                                                                    'aword2':archive.aword2, 
                                                                                    'aword3':archive.aword3})
            elif archive.archive_type == "INSTITUTION":
                form2 = AccountSettingsFormInstitutionalArchive(instance=archive, initial={
                    
                                                                                    'archive_slug': archive.archive_slug,
                                                                                    'bio': archive.bio,
                                                                                    'insta_link': archive.insta_link,
                                                                                    'fb_link': archive.fb_link,
                                                                                    'twitter_link':archive.twitter_link,
                                                                                    'institution_name':archive.institution_name,
                                                                                    'institution_website':archive.institution_website,
                                                                                    })


        if 'privacy_settings' in request.POST:
            # if the submitted form is the privacy settings form
            form3 = AccountSettingsFormPrivacy(request.POST, instance=archive)

            if form3.is_valid():
                form3.save()

        else:
            # if the submitted form is not the privacy settings form
            form3 = AccountSettingsFormPrivacy(instance=archive, initial={'private': archive.private})

        if 'contact_us' in request.POST:
            #if the submitted form is the contact us form
            form4 = AccountSettingsFormContact(request.POST)

            if form4.is_valid():
                ## send contact us email.
                pass

        else:
            # if the submitted form is not the contact us form
            form4 = AccountSettingsFormContact()

    else:
        # if no form is submitted (page is loaded for example)
        form1 = AccountSettingsFormUser(instance=request.user, initial={'username': request.user.username, 
                                                                        'email': request.user.email
                                                                        })

        if archive.archive_type == "ARTIST":
            form2 = AccountSettingsFormArtistArchive(instance=archive, initial={
                                                                                'archive_slug': archive.archive_slug, 
                                                                                'bio': archive.bio, 
                                                                                'insta_link': archive.insta_link, 
                                                                                'fb_link': archive.fb_link, 
                                                                                'twitter_link':archive.twitter_link, 
                                                                                'first_name':archive.first_name, 
                                                                                'last_name':archive.last_name, 
                                                                                'aword1':archive.aword1, 
                                                                                'aword2':archive.aword2, 
                                                                                'aword3':archive.aword3})
        elif archive.archive_type == "INSTITUTION":
            form2 = AccountSettingsFormInstitutionalArchive(instance=archive, initial={
                                                                                'archive_slug': archive.archive_slug,
                                                                                'bio': archive.bio,
                                                                                'insta_link': archive.insta_link,
                                                                                'fb_link': archive.fb_link,
                                                                                'twitter_link':archive.twitter_link,
                                                                                'institution_name':archive.institution_name,
                                                                                'institution_website':archive.institution_website,
                                                                                })

        form3 = AccountSettingsFormPrivacy(instance=archive, initial={'private': archive.private})
        form4 = AccountSettingsFormContact
        
    return render(request, "accounts/account_settings.html", {"archive": archive, "UserForm":form1, "ArchiveForm":form2, "PrivacyForm":form3, "ContactForm":form4})



# def login(request):
#     if request.method == "POST":
#         # if the form is submitted
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             # if the inputs are all valid, log in existing user
#             form.save()
#             # then redirect home
#             return redirect('index')
#     else:
#         form = LoginForm()

#     return render(request, "accounts/login.html", {"form": form})

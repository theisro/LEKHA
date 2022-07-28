from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import OnboardingForm, UserRegisterForm
from archival.models import Archive, Folder

from django.contrib.auth.views import LoginView    

from django.contrib.auth import logout

from django.core.files.storage import FileSystemStorage

import secrets #for generating random slugs (for now, remove when redundant)


# Create your views here.

# class AdminLogin(LoginView):
#     template_name = "accounts/login.html"

def handle_uploaded_archive_file(f):  
    path = 'files/archive'+f.name
    with open(path, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)
        
    return path

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
            filesystem = Folder.add_root(name="{}'s filesystem".format(archive_slug), archive=archive)

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

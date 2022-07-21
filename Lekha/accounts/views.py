from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import OnboardingForm, UserRegisterForm
from archival.models import Archive, Folder

from django.contrib.auth.views import LoginView    


# Create your views here.

# class AdminLogin(LoginView):
#     template_name = "accounts/login.html"


def onboarding(response):
    if response.method == "POST":
        # if the form has been submitted
        # Serve the form -> response.POST
        form = OnboardingForm(response.POST)

        if form.is_valid():
            # if the all the fields on the form pass validation
            # retrieve information from the form
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            aword1 = form.cleaned_data.get("aword1")
            aword2 = form.cleaned_data.get("aword2")
            aword3 = form.cleaned_data.get("aword3")
            bio = form.cleaned_data.get("bio")
            insta_link = form.cleaned_data.get("insta_link")
            fb_link = form.cleaned_data.get("fb_link")
            twitter_link = form.cleaned_data.get("twitter_link")
            archive_image = form.cleaned_data.get("archive_image")
            cv = form.cleaned_data.get("cv")


            ### these variables need to be dynamically assigned and/or properly retrieved from the html. 
            archive_slug = "asd"
            private = False
            archive_type="ARTIST"

            # create a new archive with the parameters retrieved from the form. currently logged in user is automatically linked
            archive = Archive(first_name=first_name,
                            last_name=last_name,
                            aword1=aword1,
                            aword2=aword2,
                            aword3=aword3,
                            bio=bio,
                            insta_link=insta_link,
                            fb_link=fb_link,
                            twitter_link=twitter_link,
                            cv = cv,
                            archive_image=archive_image,
                            private=private,
                            archive_type=archive_type,
                            archive_slug=archive_slug,
                            )

            # save the archive to the database (save also assigns timestamps to the archive: created, modified)
            archive.save() 

            ## step 2 create filesystem and link it to the archive
            filesystem = Folder.add_root(name="{}'s filesystem".format(archive_slug), archive=archive)
            # category1 = Folder.objects.get(pk=filesystem.pk).add_child(name='Paintings')
            # series1 = Folder.objects.get(pk=category1.pk).add_child(name='Oil Paintings')

        # Redirect to index page
        return redirect('index')

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

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import OnboardingForm, UserRegisterForm
from .models import Artist

# Create your views here.


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
            insta_handle = form.cleaned_data.get("insta_handle")
            fb_handle = form.cleaned_data.get("fb_handle")
            twitter_handle = form.cleaned_data.get("twitter_handle")
            private = form.cleaned_data.get("private")

            # create a new artist with the parameters retrieved from the form
            artist = Artist(first_name=first_name,
                            last_name=last_name,
                            aword1=aword1,
                            aword2=aword2,
                            aword3=aword3,
                            bio=bio,
                            insta_handle=insta_handle,
                            fb_handle=fb_handle,
                            twitter_handle=twitter_handle,
                            private=private)

            # create a new artist with parameters from form, assign it to the current user
            reponse.user.artist.add(artist)
            # artist.save()

        # Redirect to index page
        return HttpResponseRedirect("")

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
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, "accounts/register.html", {"form": form})

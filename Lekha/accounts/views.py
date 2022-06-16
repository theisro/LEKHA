from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import OnboardingForm, SignupForm
from .models import Artist

from django.contrib.auth import login, authenticate

#delete when done
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def onboarding(response):
    if response.method == "POST":
        form = OnboardingForm(response.POST)

        if form.is_valid():
            ## retrieve information from the form
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

            ## create a new artist with the parameters retrieved from the form
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

            ## save the artist to the database
            artist.save()
        
        ## Redirect to dashboard page
        return HttpResponseRedirect("")

    else:
        form = OnboardingForm()

    return render(response, "accounts/onboarding.html", {"form":form})
            

def signup(response):
    if response.method == "POST":
        # form = SignupForm(response.POST)
        form = UserCreationForm(response.POST)

        if form.is_valid():
            form.save()
        else:
            return redirect("/onboarding")

        # return redirect("/onboarding")
    else:
        # form = SignupForm()
        form = UserCreationForm()
    
    return render(response, "accounts/signup.html", {"form":form})
"""Lekha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from accounts import views as account_views
from main import views as main_views
from archival import views as archival_views
from django.contrib.auth import views as auth_view
from django.contrib.staticfiles.storage import staticfiles_storage

from accounts.forms import LoginForm

urlpatterns = [
    ## FUNCTIONAL VIEWS 
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url("main/favicon.ico"))), # browser looks for favicon.ico in root folder, redirect to static folder. Functional, not a view
    

    ## HTML PAGE URLS
    path('admin/', admin.site.urls),


    # account views
    path('onboarding/', account_views.onboarding, name='onboarding'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(authentication_form=LoginForm, template_name='accounts/login.html'), name="login"),
    path('logout/', account_views.logout_view, name='logout'),
    path('account_settings/', account_views.account_settings, name='account_settings'),

    # archival views
    path('dashboard/', archival_views.dashboard, name='dashboard'),

    # main views
    path('features/', main_views.features, name='features'),
    path('about/', main_views.about, name='about'),
    path('partners/', main_views.partners, name='partners'),
    path('report/', main_views.report, name='report'),
    path('contact/', main_views.contact, name='contact'),
    path('<str:slug>/', main_views.archive, name='archive'), # --> add custom verification to make sure users cant choose the 'restricted words' as their slug
    path('item/<str:slug>/', main_views.work, name='work'),
    path('', main_views.index, name='index'),



    ## METHODS (for multi page app -> shift to htmx patterns or react patterns when SPA functionality is built)
    # path('dashboard/edit_work/<str:work_slug>/', archival_views.edit_work, name='edit_work'),
    path('dashboard/add_work/<int:folder_pk>/', archival_views.add_work, name='add_work'),
    path('dashboard/add_media_to_work/<int:work_pk>', archival_views.add_media_to_work, name='add_media_to_work'),
    path('dashboard/add_folder/<int:folder_pk>', archival_views.add_folder, name='add_folder'),
]

htmx_patterns = [
    path('add_folder/<int:pk>', archival_views.add_folder, name='add_folder'),
    path('delete_folder/<int:pk>', archival_views.delete_folder, name='delete_folder'),
    path('delete_work/<int:pk>', archival_views.delete_work, name='delete_work'),
    # path('add_work/<int:pk>', archival_views.add_work, name='add_work'), 
]


urlpatterns += htmx_patterns

# these enable the serving of static and media content to the website during development.
# This needs to be changed to our cloud storage option during production (if settings.DEBUG=False)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)



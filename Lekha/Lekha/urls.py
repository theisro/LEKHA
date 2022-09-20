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
from django.conf.urls.static import static
from accounts import views as account_views
from main import views as main_views
from archival import views as archival_views
from django.contrib.auth import views as auth_view

from accounts.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='index'),
    path('onboarding/', account_views.onboarding, name='onboarding'),
    path('register/', account_views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(authentication_form=LoginForm, template_name='accounts/login.html'), name="login"),
    path('logout/', account_views.logout_view, name='logout'),
    path('dashboard/', archival_views.dashboard, name='dashboard'),
    path('account_settings/', account_views.account_settings, name='account_settings'),
    path('<str:slug>/', main_views.archive, name='archive'),
    path('item/<str:slug>/', main_views.work, name='work'),
]

htmx_patterns = [
    path('add_folder/<int:pk>', archival_views.add_folder, name='add_folder'),
    path('delete_folder/<int:pk>', archival_views.delete_folder, name='delete_folder'),
    # path('add_work/<int:pk>', archival_views.add_work, name='add_work'),
    # path('delete_work/<int:pk>', archival_views.delete_work, name='delete_work'),
]

urlpatterns += htmx_patterns

# these enable the serving of static and media content to the website
# during development. This needs to be changed to something more robust during production.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)


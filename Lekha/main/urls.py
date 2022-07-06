from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact')
]

from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('report/', views.report, name='report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

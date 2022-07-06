from django.contrib import admin
from .models import ArtistArchive, InstituionalArchive

# Register your models here. Registering allows us to see models on the admin panel. For example, you can see all the different archive instances on lekha.
admin.site.register(ArtistArchive) 
admin.site.register(InstituionalArchive)
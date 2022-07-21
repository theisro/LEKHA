from django.contrib import admin
from .models import Archive, Work, Folder, MediaFile

# Register your models here. Registering allows us to see models on the admin panel. For example, you can see all the different archive instances on lekha.
admin.site.register(Archive) 
admin.site.register(Work)

# do we want to register these?
admin.site.register(Folder)
admin.site.register(MediaFile)
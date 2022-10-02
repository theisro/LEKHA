from django.contrib import admin
from .models import Archive, Work, Folder, MediaFile
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


# Register your models here. Registering allows us to see models on the admin panel. For example, you can see all the different archive instances on lekha.
admin.site.register(Archive) 
admin.site.register(Work)

# do we want to register these?
admin.site.register(MediaFile)

# Hierarchical data registration
class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Folder)

admin.site.register(Folder, MyAdmin)
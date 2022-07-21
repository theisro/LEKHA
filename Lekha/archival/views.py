from django.shortcuts import render
from django.http import HttpResponse

from .models import Archive, Folder

# middleware for getting the currently logged in user
from crum import get_current_user



# Create your views here.
def dashboard(request):
    user = get_current_user()
    archive = Archive.objects.get(creator=user)
    filesystem = Folder.objects.get(archive=archive)
    return HttpResponse('archive: {}, filesystem: {}, \n Filesystem: {}'.format(archive.archive_slug, filesystem.name, Folder.dump_bulk()))

from django.shortcuts import render

from django.http import HttpResponse

from archival.models import ArtistArchive

# Create your views here.

def index(request):
    return render(request, 'index.html')


def features(request):
    return render(request, 'features.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def partners(request):
    return render(request, 'partners.html')


def report(request):
    return render(request, 'report.html')

def archive(request, archive_id):
    # archive = #retrieve archive with id=archive_id
    # archive = Archive.objects.get(archive_name=archive_id)

    # return render(request, 'archive.html', {'archive': archive})
    return HttpResponse("You're looking at %s's archive." % archive_id)


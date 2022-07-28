from django.shortcuts import render, redirect

from django.http import HttpResponse

from archival.models import Archive, Folder

# mail sending
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def index(request):
    return render(request, 'index.html')


def features(request):
    return render(request, 'features.html')


def about(request):
    return render(request, 'about.html')


def partners(request):
    return render(request, 'partners.html')


def archive(request, slug):
    # retrieve archive with the corresponding slug requested (lekha.cc/dhruva will request the archive with slug='dhruva')
    archive = Archive.objects.get(archive_slug=slug)
    filesystem = Folder.objects.get(archive=archive)
    return render(request, 'archive.html', {'archive': archive, 'filesystem': filesystem})


def workPage(request):
    # testing work page
    return render(request, 'workPage.html')


def report(request):
    return render(request, 'report.html')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Lekha Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    form = ContactForm()
    return render(request, "contact.html", {'form': form})

from django.shortcuts import render, redirect

from django.http import HttpResponse

from archival.models import Archive

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


def artistPage(request):
    # testing artist page
    return render(request, 'artistPage.html')


def workPage(request):
    # testing work page
    return render(request, 'workPage.html')


def report(request):
    return render(request, 'report.html')


def archive(request, archive_id):
    # retrieve archive which has the slug archive_id
    # archive = Archive.objects.get(archive_slug=archive_id)

    # render the HTML of the archive display page, and pass in data of the archive we retrieved above. 
    return render(request, 'artistPage.html')


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

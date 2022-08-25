from django.shortcuts import render, redirect

from django.http import HttpResponse

from archival.models import Archive, Folder, Work, MediaFile

# mail sending
from .forms import ContactForm, BugReportForm
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
    # retrieve archive with the corresponding slug requested (lekha.cc/dhruva will return the archive with slug='dhruva')
    archive = Archive.objects.get(archive_slug=slug)
    filesystem = Folder.objects.get(archive=archive)
    return render(request, 'archive.html', {'archive': archive, 'filesystem': filesystem})

def work(request, slug):
    # retrieve work with the corresponding slug requested (lekha.cc/item/22344 will return the archive with slug='22344')
    # work slugs are uniqu alphanumeric codes corresponding to their "archival id" within the lekha archival system.
    work = Work.objects.get(work_slug=slug)
    # media_list = MediaFile.objects.get(work=work)
    media_list = None
    # get ordered list of folder structure (archive > folder 1 > ... > folder n > work_name) and return this as a list for the page
    ## TBD
    return render(request, 'work.html', {'work': work, 'media_list': media_list})


def workPage(request):
    # testing work page
    return render(request, 'workPage.html')


def report(request):
    '''Send bug report email to admin, using the BugReportForm and report.html'''
    if request.method == 'POST':
        form = BugReportForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "Lekha Bug Report"
            body = {
                'email': form.cleaned_data['email_address'],
                'bug_report': form.cleaned_data['bug_report'],
                'image': form.cleaned_data['image'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    form = BugReportForm()
    return render(request, 'report.html', {'form': form})

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

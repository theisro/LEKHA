from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import WorkForm
from django.forms import modelformset_factory


from .models import Archive, Folder, Work, MediaFile

# middleware for getting the currently logged in user
from crum import get_current_user

# decorator to enforce that users need to be logged in to access some pages
from django.contrib.auth.decorators import login_required



## helper functions
def get_archival_id():
    '''
    Generate a unique archival id for a work.
    The archival id is a string of the form "LAWXXXXXX" where L stands for Lekha, A stands for archive, W stands for work, and XXXXXX is a 6 digit number that is incremented everytime a new work is created.
    '''
    # get the last work that was added to the database
    last_work = Work.objects.last()
    if last_work is None:
        # if there are no works in the database, start with LAW000001
        return "LAW000001"
    else:
        # otherwise, get the archival id of the last work and increment it by 1
        last_id = last_work.work_slug
        last_id = last_id[3:]
        last_id = int(last_id)
        last_id += 1
        last_id = str(last_id)
        last_id = last_id.zfill(6)
        return "LAW" + last_id

def get_filesystem_structure(folder):
    '''
    Get a custom data structure that represents the filesystem's structure as well as it's constituent works.

    presented in a format that is easy for the html template to parse.

    filesystem_pk: the primary key of the filesystem
    '''
    # filesystem = Folder.objects.get(pk=filesystem_pk)
    filesystem_structure = folder.get_annotated_list(folder)

    file_list = []

    for folder, info in filesystem_structure:
        divider = string_val = "-" * int(info['level'])
        

        work_list=[]
        work_divider = divider + "-"
        for work in Work.objects.filter(folder=folder):
            work_info = {'divider': work_divider}
            work_list.append((work, work_info))
        
        new_info = {'open': info['open'], 'close':info['close'], 'level': info['level'], 'divider': divider, 'works': work_list}

        file_list.append((folder, new_info))

    return file_list

@login_required
def dashboard(request):
    '''
    The dashboard is the main page of the archival app. It shows the filesystem of the logged in user.

    If the user is not logged in, they are redirected to the login page.

    If the user is logged in, they are shown the filesystem of the archive that they created.
    '''
    # check if the user is logged in
    user = get_current_user()

    if user.is_authenticated:
        archive = Archive.objects.get(creator=user)
        filesystem = Folder.objects.get(archive=archive)            
        
        return render(request, "archival/dashboard.html", {'filesystem': filesystem, "archive": archive, "fileSystemParse": get_filesystem_structure(filesystem)})
    else:
        return redirect('login')




@login_required
def add_folder(request, folder_pk):
    '''
    Add a folder to the filesystem.
    pk: the primary key of the parent folder
    name: the name of the new folder
    Asynchronous view that is triggered on the dashboard without reloading the page.
    '''
    # add folder to the database
    parent = Folder.objects.get(pk=folder_pk)

    if request.method == "POST" and parent.creator == get_current_user():
            folder_name = request.POST['folderName']
            parent.add_child(name=folder_name)

            return redirect('dashboard')

    # # return the template fragment --> to be used in single page app
    # filesystem = Folder.objects.get(archive=Archive.objects.get(creator=get_current_user()))
    # return render(request, "partials/folder_view.html", {'fileSystemParse': filesystem.get_annotated_list()})

    return render(request, "archival/add_folder.html")

def delete_folder(request, pk):
    '''
    Delete a folder and all of its children.
    Asynchronous view that is triggered on the dashboard without reloading the page.
    TBD: make sure people cannot randomly delete folders through the url. 
    -> make the folder only get deleted if the logged in user is the creator of the folder.
    '''
    # delete folder from the database
    folder = Folder.objects.get(pk=pk)
    folder.delete()
    
    # return the template fragment
    filesystem = Folder.objects.get(archive=Archive.objects.get(creator=get_current_user()))
    return render(request, "partials/folder_view.html", {'fileSystemParse': get_filesystem_structure(filesystem)})

@login_required
def add_work(request, folder_pk):
    '''
    Add a work to the filesystem.

    folder_pk: the primary key of the parent folder

    Checks if the user is logged in and if the user is the creator of the folder. If so, the user is allowed to add a work to the folder. Otherwise, the user is redirected to the login page.
    '''
    # add work to the database
    parent = Folder.objects.get(pk=folder_pk)
    # mediaFormSet = modelformset_factory(MediaFile, fields=('name', 'alt_text', 'caption', 'media'), extra=1)

    

    if request.method == "POST" and parent.creator == get_current_user():
        # if the form has been submitted
        # Serve the form -> request.POST
        form = WorkForm(request.POST)
        # mediaFormSet = mediaFormSet(request.POST)

        if form.is_valid(): # if the all the fields on the form pass validation

            # Generate archival ID for work
            # archival ID is random, unique 6 digit number that identifies the work
            archival_id = get_archival_id()

            # create a new work with the parameters retrieved from the form. currently logged in user is automatically linked
            work = form.save(commit=False)
            work.work_slug = archival_id
            work.folder=parent
            work.archive=parent.get_root().archive
            work.save()
            
            # Redirect to media adding page
            # return redirect('add_media_to_work', work_pk=work.pk)
            return redirect('add_media_to_work', work_pk=work.pk)

    else:
        # If the form is not submitted (page is loaded for example)
        # -> Serve the empty form
        form = WorkForm()


    return render(request, "archival/add_edit_work.html", {"workForm": form})

def delete_work(request, pk):
    '''
    Delete a work from the filesystem.

    work_pk: the primary key of the work

    Checks if the user is logged in and if the user is the creator of the work. If so, the user is allowed to delete the work. Otherwise, the user is redirected to the login page.
    '''
    work = Work.objects.get(pk=pk)

    if work.creator == get_current_user():
        # delete work from the database
        work.delete()

    # return the template fragment
    filesystem = Folder.objects.get(archive=Archive.objects.get(creator=get_current_user()))
    return render(request, "partials/folder_view.html", {'fileSystemParse': get_filesystem_structure(filesystem)})

@login_required
def add_media_to_work(request, work_pk):
    '''
    Add media to a work.

    work_pk: the primary key of the work

    Checks if the user is logged in and if the user is the creator of the work. If so, the user is allowed to add media to the work. Otherwise, the user is redirected to the login page.
    '''
    # define mediaFile formset (repeatable form)
    work = Work.objects.get(pk=work_pk)
    mediaFormSet = modelformset_factory(MediaFile, fields=('name', 'alt_text', 'caption', 'media'))

    if request.method == "POST" and work.creator == get_current_user():
        # if the form has been submitted
        # Serve the form -> request.POST
        form = mediaFormSet(request.POST, request.FILES)

        if form.is_valid(): # if the all the fields on the form pass validation

            # iterate over all the files that the user has uploaded and save them to the database, and link them to the work
            instances = form.save(commit=False)

            for instance in instances: ## wouldnt there just be 1 submitted form? --> redundant for loop>
                instance.work = work
                instance.save()

            # Redirect to dashboard page
            # return redirect('dashboard')

    # If the form is not submitted (page is loaded for example)
    # -> Serve the empty form
    form = mediaFormSet(queryset=MediaFile.objects.filter(work=work))
    # form = mediaFormSet(queryset=MediaFile.objects.none())


    return render(request, "archival/add_media_to_work.html", {"form": form, "work_name": work.name})

def delete_media(request, media_pk):
    '''
    Delete media from a work.

    media_pk: the primary key of the media

    Checks if the user is logged in and if the user is the creator of the media file. If so, the user is allowed to delete media from the work. Otherwise, the user is redirected to the login page.
    '''
    media = MediaFile.objects.get(pk=media_pk)
    work = media.work

    if media.creator == get_current_user():

        # delete media from the database
        media.delete()

        # Redirect to media adding page
        return redirect('add_media_to_work', work_pk=work.pk)
    else:
        return redirect('login')


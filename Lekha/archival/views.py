from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import WorkForm


from .models import Archive, Folder, Work, MediaFile

# middleware for getting the currently logged in user
from crum import get_current_user

# decorator to enforce that users need to be logged in to access some pages
from django.contrib.auth.decorators import login_required

# # dashboard methods
# def delete_folder(request, folder_id):
#     folder = Folder.objects.get(id=folder_id)
#     folder.delete()

#     return HttpResponseRedirect('/dashboard')

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
        last_id = last_work.archival_id
        last_id = last_id[3:]
        last_id = int(last_id)
        last_id += 1
        last_id = str(last_id)
        last_id = last_id.zfill(6)
        return "LAW" + last_id

@login_required
def delete_folder(request):
    if request.is_ajax():
        folder = request.POST['folder_id']

        folder = Folder.objects.get(id=folder_id)
        folder.delete()
        return redirect('dashboard')



# Create your views here.
def dashboard(request):
    user = get_current_user()
    archive = Archive.objects.get(creator=user)
    filesystem = Folder.objects.get(archive=archive)

    if request.method == "POST":
        if 'addCategory' in request.POST:
            category_name = request.POST['folderName']
            filesystem = Folder.objects.get(pk=filesystem.pk)
            filesystem.add_child(name=category_name)
            
    
    return render(request, "archival/dashboard.html", {'filesystem': filesystem, "archve": archive, "fileSystemParse": filesystem.get_annotated_list()})


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
    return render(request, "partials/folder_view.html", {'fileSystemParse': filesystem.get_annotated_list()})

def add_folder(request, pk, name):
    '''
    Add a folder to the filesystem.

    pk: the primary key of the parent folder
    name: the name of the new folder

    Asynchronous view that is triggered on the dashboard without reloading the page.
    '''
    # add folder to the database
    parent = Folder.objects.get(pk=pk)
    parent.add_child(name=name)

    # return the template fragment
    filesystem = Folder.objects.get(archive=Archive.objects.get(creator=get_current_user()))
    return render(request, "partials/folder_view.html", {'fileSystemParse': filesystem.get_annotated_list()})


def add_work(request, folder_pk):
    '''
    Add a work to the filesystem.

    folder_pk: the primary key of the parent folder

    Checks if the user is logged in and if the user is the creator of the folder. If so, the user is allowed to add a work to the folder. Otherwise, the user is redirected to the login page.
    '''
    # add work to the database
    parent = Folder.objects.get(pk=folder_pk)

    if response.method == "POST" and parent.archive.creator == get_current_user():
        # if the form has been submitted
        # Serve the form -> response.POST
        form = WorkForm()

        if form.is_valid(): # if the all the fields on the form pass validation

            # automatically generate archival ID for work
            # archival ID is random, unique 6 digit number that identifies the work
            archival_id = get_archive_id()

            # create a new work with the parameters retrieved from the form. currently logged in user is automatically linked
            work = Work(folder=parent,
                        work_slug=archival_id,
                        name=form.cleaned_data.get("name"),
                        year=form.cleaned_data.get("year"),
                        medium=form.cleaned_data.get("medium"),
                        description=form.cleaned_data.get("description"),
                        authors=form.cleaned_data.get("authors"),
                        classification=form.cleaned_data.get("classification"),
                        location=form.cleaned_data.get("location"),
                        link=form.cleaned_data.get("link"),
                        record_creator=form.cleaned_data.get("record_creator"),
                        cd1_name=form.cleaned_data.get("cd1_name"),
                        cd1_value=form.cleaned_data.get("cd1_value"),
                        cd2_name=form.cleaned_data.get("cd2_name"),
                        cd2_value=form.cleaned_data.get("cd2_value"),
                        cd3_name=form.cleaned_data.get("cd3_name"),
                        cd3_value=form.cleaned_data.get("cd3_value"),
                        cd4_name=form.cleaned_data.get("cd4_name"),
                        cd4_value=form.cleaned_data.get("cd4_value"),
                        cd5_name=form.cleaned_data.get("cd5_name"),
                        cd5_value=form.cleaned_data.get("cd5_value"),
                        cd6_name=form.cleaned_data.get("cd6_name"),
                        cd6_value=form.cleaned_data.get("cd6_value"),
                        cd7_name=form.cleaned_data.get("cd7_name"),
                        cd7_value=form.cleaned_data.get("cd7_value"),
                        )
            # save the archive to the database (save also automatically assigns timestamps, and the user to the archive: created, modified, creator)
            work.save()

            # iterate over all the files that the user has uploaded and save them to the database, and link them to the work
            for media_file in response.FILES:
                mediaObject = MediaFile(work=work,
                                    #    folder=folder,
                                        name=media_file.name,
                                        alt_text=media_file.alt_text,
                                        caption=media_file.caption,
                                        media=media_file.media,
                                        )
                
                mediaObject.save()

            # Redirect to dashboard page
            return redirect('dashboard')

    else:
        # If the form is not submitted (page is loaded for example)
        # -> Serve the empty form
        form = WorkForm()

    return render(response, "accounts/add_work.html", {"form": form})


def add_work(request, folder_pk):
    '''
    Add a work to the filesystem.

    folder_pk: the primary key of the parent folder

    Checks if the user is logged in and if the user is the creator of the folder. If so, the user is allowed to add a work to the folder. Otherwise, the user is redirected to the login page.
    '''


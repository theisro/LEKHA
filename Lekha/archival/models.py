from django.db import models
from django.urls import reverse  # new
from django.contrib.auth.models import User
from django.utils import timezone

# library for hierarchical filesystems (file browser)
from treebeard.mp_tree import MP_Node

# middleware for getting the currently logged in user. This is necessary for assigning the 'creator' attribute of several models.
from crum import get_current_user



# Create your models here.
class Archive(models.Model):
    '''
    Contains all the metadata and pertinent info relevant to an archive. 
    There are a few different archive types, each of which has metadata that is relevant to only those archive types,
    for example artist archives are an archive of an individual's work, and will therefore have fields such as first name, cv, etc.

    '''
    ## core
    #Archive Types
    ARCHIVE_TYPE_CHOICES = (
        ('ARTIST', 'Artist'),
        ('INSTITUTION', 'Institution'),
        ('COLLECTIVE', 'Collective')
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   default=None)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    archive_slug = models.SlugField(max_length=50, null=True) # slug
    archive_type = models.CharField(  # new
        choices=ARCHIVE_TYPE_CHOICES,
        max_length=20,
        verbose_name="type of archive",
        default="ARTIST",
    )
    private = models.BooleanField(default=True)



    ## common to all archive types
    bio = models.CharField(max_length=600) # description for institutions
    insta_link = models.URLField(null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    archive_image = models.ImageField(null=True, blank=True)

    ## specific to artist archives
    first_name = models.CharField(max_length=50) # note: null=True shouldnt be set for char fields as "" is valid as null
    last_name = models.CharField(max_length=50) #blank = False prevents people from leaving fields empty in forms
    aword1 = models.CharField(max_length=20)
    aword2 = models.CharField(max_length=20)
    aword3 = models.CharField(max_length=20)
    cv = models.FileField(null=True)

    ## specific to institutional archives
    institution_name = models.CharField(max_length=50)
    institution_website = models.URLField(null=True, blank=True)

    ## 

    class Meta:
        verbose_name = "archive"
        verbose_name_plural = "archives"


    def __str__(self):
        return 'Archive: {}'.format(self.archive_slug)

    # def get_absolute_url(self): # new
    #     return reverse("", args=[str(self.archive_name)])

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        user = get_current_user()

        if not self.id: # if the model is being created for the first time:
            self.creator = user # assign the currently logged in user as the creator
            self.created = timezone.now() # set the 'created' field to the current date and time
        self.modified = timezone.now() # set the modified field to the current date and time. This is reassigned everytime the model is updated.

        return super(Archive, self).save(*args, **kwargs)

    

    
class Folder(MP_Node):
    '''
    MP_Node uses raw SQL queries so you have to 'reload' a node each time you want to add children or siblings.
    For example, you cant do

    filesystem = Folder.add_root(name = "Archive0")
    node = filesystem.add_child(name="Paintings")

    Instead you have to retrieve the node again:

    filesystem = Folder.add_root(name = "Archive0")
    paintings = Folder.objects.get(filesystem.pk).add_child(name="Paintings")

    '''
    name = models.CharField(max_length=30)
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, null=True, blank=True, default=None)

    # tree specific attributes
    node_order_index = models.IntegerField(
        blank=True,
        default=0,
        editable=False
    )
    
    # !!! this should NOT be changed after the first node is created.
    node_order_by = ['node_order_index', 'name']

    def __str__(self):
        return 'Folder: {}'.format(self.name)



class Work(models.Model):
    ## core data
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   default=None)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    work_slug = models.SlugField(max_length=50) # slug -> TBD: find way to assign default value to slug = archival number.

    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)


    # superfolder -> replaces category, series etc with dynamic hierarchical database
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    

    # basic metadata fields
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    description = models.CharField(max_length=1200, blank=True, null=True)

    # optional metadata
    authors = models.CharField(max_length=50, blank=True, null=True)
    classification = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(max_length=50, blank=True, null=True)
    record_creator = models.CharField(max_length=50, blank=True, null=True) # revisit -> 

    # custom descriptors
    cd1_name = models.CharField(max_length=50, blank=True, null=True)
    cd1_value = models.CharField(max_length=50, blank=True, null=True)
    cd2_name = models.CharField(max_length=50, blank=True, null=True)
    cd2_value = models.CharField(max_length=50, blank=True, null=True)
    cd3_name = models.CharField(max_length=50, blank=True, null=True)
    cd3_value = models.CharField(max_length=50, blank=True, null=True)
    cd4_name = models.CharField(max_length=50, blank=True, null=True)
    cd4_value = models.CharField(max_length=50, blank=True, null=True)
    cd5_name = models.CharField(max_length=50, blank=True, null=True)
    cd5_value = models.CharField(max_length=50, blank=True, null=True)
    cd6_name = models.CharField(max_length=50, blank=True, null=True)
    cd6_value = models.CharField(max_length=50, blank=True, null=True)
    cd7_name = models.CharField(max_length=50, blank=True, null=True)
    cd7_value = models.CharField(max_length=50, blank=True, null=True)


    # Standardized Metadata


    # Methods
    def __str__(self):
        return 'Work: {}'.format(self.name)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        user = get_current_user()

        if not self.id: # if the model is being created for the first time:
            self.creator = user # assign the currently logged in user as the creator
            self.created = timezone.now() # set the 'created' field to the current date and time
            # self.slug = **archival id of work (automatically determined)** 
        self.modified = timezone.now() # set the modified field to the current date and time. This is reassigned everytime the model is updated.

        return super(Work, self).save(*args, **kwargs)



class MediaFile(models.Model):
    # core
    #### Need to decide if media files can exist in folders or only in works ---> did we decide that the archive builder can also hold media files?
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   default=None)

    # descriptors
    alt_text = models.CharField(max_length=60)
    caption = models.CharField(max_length=60)
    media = models.FileField(upload_to='documents/') # handle filetype in views?

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        user = get_current_user()

        if not self.id: # if the model is being created for the first time:
            self.creator = user # assign the currently logged in user as the creator
            self.created = timezone.now() # set the 'created' field to the current date and time
            # self.slug = **archival id of work (automatically determined)** 
        self.modified = timezone.now() # set the modified field to the current date and time. This is reassigned everytime the model is updated.

        return super(MediaFile, self).save(*args, **kwargs)

from django.db import models
from django.urls import reverse  # new
from django.contrib.auth.models import User
from django.utils import timezone

# library for hierarchical filesystems (file browser)
from treebeard.mp_tree import MP_Node



# Create your models here.
class Archive(models.Model):
    '''
    Abstract Archive data type. It contains all of the information pertaining to an archive.
    '''
    ## core
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    archive_slug = models.SlugField(max_length=50) # slug


    ## common to all archive types
    bio = models.CharField(max_length=600) # description for institutions
    insta_link = models.URLField()
    fb_link = models.URLField()
    twitter_link = models.URLField()
    private = models.BooleanField()
    archive_image = models.ImageField()


    class Meta:
        abstract = True

    def __str__(self):
        return self.archive_name

    def get_absolute_url(self): # new
        return reverse("university_detail", args=[str(self.archive_name)])

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Archive, self).save(*args, **kwargs)




class ArtistArchive(Archive):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aword1 = models.CharField(max_length=20)
    aword2 = models.CharField(max_length=20)
    aword3 = models.CharField(max_length=20)
    cv = models.FileField()

class InstituionalArchive(Archive):
    institution_name = models.CharField(max_length=50)
    institution_website = models.URLField()

    
class Work(models.Model):
    ## core data
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    work_slug = models.SlugField(max_length=50) # slug

    # superfolder -> replaces category, series etc with dynamic hierarchical database
    # archive = models.ForeignKey(ArtistArchive, on_delete=models.CASCADE) #replace with parent folder
    

    # basic metadata fields
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    description = models.CharField(max_length=1200)

    # optional metadata
    authors = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    link = models.URLField(max_length=50)
    record_creator = models.CharField(max_length=50) # revisit -> 

    # custom descriptors
    cd1_name = models.CharField(max_length=50)
    cd1_value = models.CharField(max_length=50)
    cd2_name = models.CharField(max_length=50)
    cd2_value = models.CharField(max_length=50)
    cd3_name = models.CharField(max_length=50)
    cd3_value = models.CharField(max_length=50)
    cd4_name = models.CharField(max_length=50)
    cd4_value = models.CharField(max_length=50)
    cd5_name = models.CharField(max_length=50)
    cd5_value = models.CharField(max_length=50)
    cd6_name = models.CharField(max_length=50)
    cd6_value = models.CharField(max_length=50)
    cd7_name = models.CharField(max_length=50)
    cd7_value = models.CharField(max_length=50)


    # Standardized Metadata


    # Methods
    def __str__(self):
        return 'Work: {}'.format(self.name)


    
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

    # tree specific attributes
    node_order_index = models.IntegerField(
        blank=True,
        default=0,
        editable=False
    )
    
    # !!! this should NOT be changed after the first node is created.
    node_order_by = ['node_order_index', 'name']

    def __str__(self):
        return 'Category: {}'.format(self.name)

class MediaFile(models.Model):
    # core
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    # descriptors
    alt_text = models.CharField(max_length=60)
    caption = models.CharField(max_length=60)
    media = models.FileField(upload_to='documents/') # handle filetype in views?


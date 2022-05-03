# This is a first prototype for an Archive Class.
# Please add to this. What fields should it have?
# The ARCHIVE belongs to an ARTIST, an INSTITUTION or a COLLECTIVE.

# Possible fields for ARCHIVES could be:
# NAME
# OWNER
# Type of ARCHIVE = Artist, collective or Institution
# Date & Time Created
# Date & Time Modified
# Last Action(to undo - actions stored in an array so we can undo or redo actions(?)
# number of Total items(ART)
# A list of names of total items
# number of Total Folders(COLLECTIONS or whatever we chose to name FOLDERS)
# A list of names of Total Folders
# number of owners
# Names and list of co-owners
# Status of Archive(PRIVATE or PUBLIC)
# Type of encryption applied.
# List of HASH, KEYS associated with the archive encryption.

from django.db import models
   from django.utils import timezone
   from django.contrib.auth.models import User
   class Archive(models.Model):
       STATUS_CHOICES = (
           ('draft', 'Draft'),
           ('published', 'Published'),
       )
         
         #Archive Types
           ARCHIVE_TYPE = (
           ('artist, 'Artist'),
           ('Institution', 'Institution'),
            ('Collective', 'Collective')
       )
         
         
         
       title = models.CharField(max_length=250)
       slug = models.SlugField(max_length=250,
                               unique_for_date='publish')
       author = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='Archive_owner')
       ArchiveDescription = models.TextField()
       publish = models.DateTimeField(default=timezone.now)
       created = models.DateTimeField(auto_now_add=True)
       updated = models.DateTimeField(auto_now=True)
       status = models.CharField(max_length=10,
                                 choices=STATUS_CHOICES,
                                 default='draft')
              ArchiveType = models.CharField(max_length=10,
                                 choices=ARCHIVE_TYPE,
                                 default='Artist')
              
             class Meta:
           ordering = ('-publish',)
       def __str__(self):
           return self.title

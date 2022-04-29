# This is a first prototype for an Archive Class.
# Please add to this. What fields should it have?
# The ARCHIVE belongs to an ARTIST, an INSTITUTION or a COLLECTIVE.




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

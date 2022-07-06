# The USER exits.
# The USER creates ARCHIVES.
# The USER is given access to ARCHIVES.
# Some USERs can access multiple ARCHIVES.

#  ******** FEATURES ***********
# “An authentication mechanism for verifying the user's identity”
# “All users are identified by a unique number called the User ID, or UID.”
# All users can belong to a USER GROUP which has a unique ID which can be used to access multiple archives.
# IS there a SUPERUSER? Where does this go?


from django.db import models
   from django.utils import timezone
   from django.contrib.auth.models import User
   
  
    class Users(models.Model):
    
     Name = models.CharField(max_length=250)
     Email = models.CharField(max_length=250)

     slug = models.SlugField(max_length=250,
                               unique_for_date='publish')
     UID = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='Archive_owner')
   # User Group id
       UID = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='Archive_owner')
       
        ArchiveDescription = models.TextField()
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10,
                                 choices=STATUS_CHOICES,
                                 default='draft')
      
              
            



from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
   title = models.CharField(max_length=200)
   description = RichTextField()
   image = models.ImageField(blank=True)
   date  = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.title
   

class ContactInformation(models.Model):
   
   address = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   email  = models.EmailField()
   opening_hour = models.CharField(max_length=200)

   def __str__(self):
      return self.email
   
   
class ContactMessage(models.Model):
   name  = models.CharField(max_length = 200)
   email  =  models.EmailField()
   subject  = models.CharField(max_length=200)
   message = models.TextField()
   
   def __str__(self):
      return self.name+"name"
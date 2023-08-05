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
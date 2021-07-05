from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Contactdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    message=models.TextField()

    def __str__(self):
        return self.name



class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField()
    content=RichTextField()
    author=models.CharField(max_length=50,default=True)
    posted_date=models.DateTimeField(auto_now_add=True)
     

from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title=models.CharField( max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=100)
    image=models.FilePathField(path="/img/",editable=False)
    githublink=models.CharField(max_length=100,default="#")

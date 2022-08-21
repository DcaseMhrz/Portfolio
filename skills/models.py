from django.db import models

# Create your models here.


class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    skillweight=models.IntegerField(default=1)

from django.db import models
from django.db.models import CharField
from django.utils import timezone


# Create your models here.
class TodoItem(models.Model):
     content=models.CharField(max_length=200)
     cdate = models.DateField(blank=True, null=True)


     def __str__(self):
          return self.content


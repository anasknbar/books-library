from django.db import models

from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  title = models.CharField(max_length=16,blank=False,null=False)
  description = models.CharField(max_length=128,blank=False,null=False)
  rating = models.IntegerField(blank=False,null=False)
  publish_date = models.DateField(blank=False,null=False)
  
  def __str__(self):
    return f"{self.author}"
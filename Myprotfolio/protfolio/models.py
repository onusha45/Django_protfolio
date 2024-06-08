from django.db import models

# Create your models here.
class Contact(models.Model):
    fname =  models.CharField(max_length=50)
    lname =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=30)
    content =  models.CharField(max_length=200)

    def __str__(self):
         return f"{self.fname}{self.lname}"
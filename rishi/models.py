from django.db import models

# Create your models here.


class destinations(models.Model):


    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

   


   
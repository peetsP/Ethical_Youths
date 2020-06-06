from django.db import models

# Create your models here.

class TopCarousel(models.Model):
    carousel_img = models.ImageField(upload_to='pics')
    image_alt = models.CharField(max_length=15)
    carousel_desc = models.CharField(max_length=35)
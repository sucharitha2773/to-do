from django.db import models
from PIL import Image

class Style(models.Model):
    text    = models.TextField()
    image   = models.ImageField(upload_to='pics')

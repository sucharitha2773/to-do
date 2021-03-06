from django.db import models
from PIL import Image

class Post(models.Model):                         
    # author = models.for    
    content = models.CharField(max_length=50)
    text    = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    image   = models.ImageField(upload_to='pics',null=True, blank=True)




from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    statuses = [("D","Draft"),("P","Published")]

    title = models.CharField(max_length = 250, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=statuses,default="D")
    #published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='blog/')
    slug = models.SlugField(blank=True)
    #author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
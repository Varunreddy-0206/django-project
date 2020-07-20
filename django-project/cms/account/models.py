from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="account/",blank = True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

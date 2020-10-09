from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFit
from imagekit.models import ImageSpecField
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='profile_photo', null=True)
    image_medium = ImageSpecField(source='profile_photo',
                                            processors=[ResizeToFit(300, 300)], format='jpeg', options={'quality': 80})
    bio = models.TextField(max_length=5000, null=True)
    

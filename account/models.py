from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.hashers import make_password
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver


class CustomUser(AbstractUser):
    username = models.CharField(
        null=True, blank=True, max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    image = CloudinaryField("user_image", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'username', 'bio']

    def __str__(self):
        return f'{self.username}'


@receiver(pre_delete, sender=CustomUser)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)

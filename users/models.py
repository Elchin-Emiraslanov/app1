from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Profile photo')
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'For user'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.username
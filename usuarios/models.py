from django.db import models
from Lab.shared.models import DefaultModel
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserApp(DefaultModel, AbstractUser):
    email = models.TextField()
    username = models.TextField()
    password = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
    
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','password']
    



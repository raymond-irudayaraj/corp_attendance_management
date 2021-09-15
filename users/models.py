from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=14)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'start_time', 'end_time','phone']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
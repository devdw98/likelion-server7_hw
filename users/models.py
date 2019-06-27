from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Post(models.Model):
    author = models.ForeignKey(CustomerUser, on_delete='CASCADE')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    url = models.URLField(max_length = 300, blank = True)
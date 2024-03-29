from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts_post_set') # 'User' is bad case.
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

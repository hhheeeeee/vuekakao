from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass
    # username = models.CharField(max_length=30)
    # nickname = models.CharField(max_length=30, blank=True, null=True)
    # email = models.EmailField(max_length=254, blank=True, null=True)
    # age = models.IntegerField(blank=True, null=True)
    # money = models.IntegerField(blank=True, null=True)
    # salary = models.IntegerField(blank=True, null=True)
    # financial_products = models.TextField(blank=True, null=True)

    # is_active = models.BooleanField(default=True)

    # USERNAME_FIELD = 'username'
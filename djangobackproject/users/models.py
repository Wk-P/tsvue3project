from django.db import models
from django.contrib.auth.models import AbstractUser
from items.models import Item


# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    

class UserItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_cart = models.BooleanField(default=False)
    is_favorate = models.BooleanField(default=False)
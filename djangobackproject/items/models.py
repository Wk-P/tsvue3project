from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.TextField(default="noname", max_length=255)
    desc = models.TextField(default=None, max_length=2048)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

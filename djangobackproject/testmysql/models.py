from django.db import models

# Create your models here.
class TestModel(models.Model):
    content = models.CharField(max_length=255, default="")
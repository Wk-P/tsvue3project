from django.contrib import admin

# Register your models here.
from items.models import Item, UserItem
admin.site.register([Item, UserItem])
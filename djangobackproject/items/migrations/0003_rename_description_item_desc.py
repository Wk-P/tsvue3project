# Generated by Django 5.0.7 on 2024-07-10 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_item_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='desc',
        ),
    ]
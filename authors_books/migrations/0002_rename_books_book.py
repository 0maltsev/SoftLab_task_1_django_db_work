# Generated by Django 3.2.9 on 2021-11-26 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors_books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-04 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_book_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='author',
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-04 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_author_publisher_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crudapp.author'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_user_phoneno_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneno',
            field=models.CharField(default='', max_length=100),
        ),
    ]

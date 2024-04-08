# Generated by Django 5.0.3 on 2024-04-04 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0017_alter_area_city_alter_area_country_alter_area_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.city'),
        ),
        migrations.AlterField(
            model_name='area',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.country'),
        ),
        migrations.AlterField(
            model_name='area',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.state'),
        ),
    ]
# Generated by Django 3.2.25 on 2024-06-18 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descontrole', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimativa',
            name='mes',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
    ]

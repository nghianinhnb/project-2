# Generated by Django 4.2.1 on 2023-07-09 13:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2023, 7, 9, 13, 45, 53, 91692, tzinfo=datetime.timezone.utc))]),
        ),
        migrations.AlterField(
            model_name='user',
            name='school_year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

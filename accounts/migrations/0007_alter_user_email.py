# Generated by Django 4.2.1 on 2023-07-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
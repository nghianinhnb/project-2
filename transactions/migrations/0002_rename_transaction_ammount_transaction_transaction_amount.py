# Generated by Django 4.2.1 on 2023-07-13 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_ammount',
            new_name='transaction_amount',
        ),
    ]
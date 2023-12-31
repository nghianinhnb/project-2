# Generated by Django 4.2.1 on 2023-07-09 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registation_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tuition_coefficient', models.DecimalField(decimal_places=2, default=1, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=12, unique=True)),
                ('subject_name', models.CharField(max_length=100)),
                ('tuition_credit', models.PositiveSmallIntegerField(default=0)),
                ('year', models.PositiveSmallIntegerField(default=2023)),
                ('semester', models.CharField(choices=[('1', 'Kỳ 1'), ('2', 'Kỳ 2'), ('3', 'Kỳ hè')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='registrated_subjects', through='subjects.Registration', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

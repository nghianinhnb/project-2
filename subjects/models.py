from django.db.models import *
from django.utils import timezone

from accounts.models import User

# Create your models here.
class Subject(Model):
    YEAR_CHOICES = (
        ('1', 'Kỳ 1'),
        ('2', 'Kỳ 2'),
        ('3', 'Kỳ hè'),
    )

    subject_id = BigAutoField(primary_key=True)
    subject_code = CharField(max_length=12, unique=True)
    subject_name = CharField(max_length=100, null=False)
    tuition_credit = PositiveSmallIntegerField(default=0)
    year = PositiveSmallIntegerField(default=timezone.now().year)
    semester = CharField(max_length=1, choices=YEAR_CHOICES)

    users = ManyToManyField(User, related_name='registrated_subjects', through='Registration')

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Registration(Model):
    registation_id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    subject = ForeignKey(Subject, on_delete=CASCADE)
    tuition_coefficient = DecimalField(max_digits=4, decimal_places=2, default=1, null=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

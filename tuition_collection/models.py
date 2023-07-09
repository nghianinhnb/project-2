from django.db.models import *
from django.utils import timezone

from subjects.models import Subject

# Create your models here.
class TuitionCollection(Model):
    tuition_collection_id = BigAutoField(primary_key=True)
    year = PositiveSmallIntegerField(default=timezone.now().year, null=False, blank=False)
    semester = CharField(max_length=1, choices=Subject.YEAR_CHOICES, null=False, blank=False)
    school_year = PositiveSmallIntegerField(null=False, blank=False)
    tuition_collection_start = DateTimeField(null=False)
    tuition_collection_end = DateTimeField(null=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

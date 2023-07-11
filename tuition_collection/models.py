from django.db.models import *
from django.utils import timezone

from subjects.models import Subject, Registration

# Create your models here.
class TuitionCollection(Model):
    tuition_collection_id = BigAutoField(primary_key=True)
    credit_fee = DecimalField(max_digits=14, decimal_places=4, default=0, null=False)
    year = PositiveSmallIntegerField(default=timezone.now().year, null=False, blank=False)
    semester = CharField(max_length=1, choices=Subject.YEAR_CHOICES, null=False, blank=False)
    school_year = PositiveSmallIntegerField(null=False, blank=False)
    tuition_collection_start = DateTimeField(null=False)
    tuition_collection_end = DateTimeField(null=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def calculate_tuition_fee(self):
        registration_set = Registration.objects.filter(
            subject__year=self.year,
            subject__semester=self.semester
        ).select_related('subject', 'user')

        tuition_fees = {}

        for registration in registration_set:
            if registration.user not in tuition_fees:
                tuition_fees[registration.user] = 0

            tuition_fees[registration.user] += registration.subject.tuition_credit * registration.tuition_coefficient * self.credit_fee

        return tuition_fees

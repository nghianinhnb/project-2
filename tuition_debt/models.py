from django.db.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import User
from subjects.models import Registration
from tuition_collection.models import TuitionCollection

# Create your models here.
class TuitionDebt(Model):
    tuition_debt_id = BigAutoField(primary_key=True)
    tuition_collection = ForeignKey(TuitionCollection, on_delete=SET_NULL, null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    ammount = DecimalField(max_digits=14, decimal_places=4, default=0, null=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


@receiver(post_save, sender=TuitionCollection)
def create_tuition_debt(sender, instance, created, **kwargs):
    if created:
        tuition_fees = instance.calculate_tuition_fee()

        tuition_debts = []
        for user, amount in tuition_fees.items():
            tuition_debts.append(TuitionDebt(
                tuition_collection=instance,
                user=user,
                amount=amount
            ))

        TuitionDebt.objects.bulk_create(tuition_debts)

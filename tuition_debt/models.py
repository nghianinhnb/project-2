from django.db.models import *
from django.utils import timezone

from accounts.models import User
from tuition_collection.models import TuitionCollection

# Create your models here.
class TuitionDebt(Model):
    tuition_debt_id = BigAutoField(primary_key=True)
    tuition_collection = ForeignKey(TuitionCollection, on_delete=SET_NULL, null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    ammount = DecimalField(max_digits=14, decimal_places=4, default=0, null=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

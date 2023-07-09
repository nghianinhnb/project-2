from django.db.models import *

from accounts.models import User

# Create your models here.
class Transaction(Model):
    transaction_id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=SET_NULL, null=True)
    transaction_method = CharField(max_length=30, null=True, blank=True)
    transaction_time = DateTimeField(null=False)
    transaction_ammount = DecimalField(max_digits=14, decimal_places=4, null=False)

    created_at = DateTimeField(auto_now_add=True)

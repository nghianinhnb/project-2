from django.db.models import *

from accounts.models import User

# Create your models here.
class Complaint(Model):
    complaint_id = BigAutoField(primary_key=True)
    sender = ForeignKey(User, related_name='sent_complaints', on_delete=SET_NULL, null=True)
    respondent = ForeignKey(User, related_name='received_complaints', on_delete=SET_NULL, null=True)
    title = CharField(max_length=100)
    content = TextField()
    response = TextField(null=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

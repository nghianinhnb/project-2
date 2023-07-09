from django.db.models import *

from accounts.models import User

# Create your models here.
class New(Model):
    new_id = BigAutoField(primary_key=True)
    author = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

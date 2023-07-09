from django.db.models import *

from accounts.models import User

# Create your models here.
class Notification(Model):
    notification_id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    is_seen = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)

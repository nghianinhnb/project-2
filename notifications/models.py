from django.db.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import User
from tuition_debt.models import TuitionDebt

# Create your models here.
class Notification(Model):
    notification_id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    is_seen = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)


@receiver(post_save, sender=TuitionDebt)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user,
            title="Tuition Debt",
            content=f"Học phí kỳ này của bạn là: {instance.ammount}"
        )

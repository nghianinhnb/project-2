from django.db.models import *
from django.utils import timezone
from django.core.validators import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, full_name, user_code, password=None):
        if not user_code:
            raise ValueError('User must have user_code')

        user = self.model(
            full_name = full_name,
            user_code = user_code,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, user_code, password=None):
        user = self.create_user(
            full_name = full_name,
            user_code = user_code,
            password = password
        )
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    user_id = BigAutoField(primary_key=True)
    user_code = CharField(max_length=10, unique=True)
    email = CharField(max_length=50, null=True, blank=True)
    full_name = CharField(max_length=50)
    dob = DateField(null=True, blank=True)
    citizen_id = CharField(max_length=12, null=True, blank=True)
    phone = CharField(max_length=20, null=True, blank=True)
    school_year = PositiveSmallIntegerField(null=True, blank=True)
    current_tuition_debt = DecimalField(max_digits=14, decimal_places=4, default=0)

    USERNAME_FIELD = 'user_code'
    REQUIRED_FIELDS = ('full_name',)

    last_login = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_superadmin = BooleanField(default=False)

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superadmin

    def has_module_perms(self, app_label) -> bool:
        return True


from tuition_debt.models import TuitionDebt

@receiver(post_save, sender=TuitionDebt)
def inc_current_tuition_debt(sender, instance, created, **kwargs):
    if created:
        instance.user.current_tuition_debt += instance.amount
        instance.user.save()


from transactions.models import Transaction

@receiver(post_save, sender=Transaction)
def des_current_tuition_debt(sender, instance, created, **kwargs):
    if created:
        instance.user.current_tuition_debt -= instance.transaction_amount
        instance.user.save()

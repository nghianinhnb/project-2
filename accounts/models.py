from django.db.models import *
from django.utils import timezone
from django.core.validators import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, full_name, user_code, email, password=None):
        if not user_code:
            raise ValueError('User must have user_code')

        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            user_code = user_code,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, user_code, email, password=None):
        user = self.create_user(
            email = email,
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
    email = CharField(max_length=50, unique=True)
    full_name = CharField(max_length=50)
    dob = DateField(null=True, blank=True, validators=[MaxValueValidator(limit_value=timezone.now())])
    citizen_id = CharField(max_length=12, null=True)
    phone = CharField(max_length=20, null=True)
    school_year = PositiveSmallIntegerField(null=True)
    current_tuition_debt = DecimalField(max_digits=14, decimal_places=4, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name', 'user_code')

    last_login = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_superadmin = BooleanField(default=False)

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superadmin

    def has_module_perms(self, app_label) -> bool:
        return True


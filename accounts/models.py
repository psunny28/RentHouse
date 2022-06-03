from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):

  def _create_user(self, email, password, **extra_fields):
    if not email:
        raise ValueError('You must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user    =   self._create_user(
        email = self.normalize_email(email),
        password = password,
        **extra_fields
    )
    user.is_active  =   True
    user.is_admin   =   True
    user.is_staff   =   True
    user.is_realtor =   True
    user.is_superuser  =   True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Profile(models.Model):
    user    =   models.OneToOneField(User, on_delete=models.CASCADE)
    gender  =   models.CharField(max_length=20, blank=True)
    address =   models.CharField(max_length=200, blank=True)
    landmark =   models.CharField(max_length=200, blank=True)
    city =   models.CharField(max_length=100, blank=True)
    state =   models.CharField(max_length=50, blank=True)
    pincode =   models.CharField(max_length=6, blank=True)
    description =   models.TextField(blank=True)
    profile_picture =   models.ImageField(upload_to='userprofile', blank=True)
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

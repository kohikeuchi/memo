
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, username=None):
        if not email:
            return ValueError('email is required')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username


class Note(models.Model):
    memo = models.TextField(max_length=500, blank=True, null=True )
    images = models.ImageField(upload_to='', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    users = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.CASCADE, null=True)
    important = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return str(self.important)



from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils import timezone

class User(models.Model):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    use_in_migrations = True
    user_email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birth = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    user_interests = models.CharField(max_length=20)
    token = models.CharField(max_length=20)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    def __str__(self):
        return f'{self.pk}, {self.user_email}, {self.password}, ' \
               f'{self.user_name}, {self.phone}, {self.birth}, {self.address},' \
               f' {self.job}, {self.user_interests}, {self.token}'

    class Meta:
        db_table = "users"
        verbose_name = 'user'
        verbose_name_plural = 'users'
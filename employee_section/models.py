from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    employee_number = models.CharField(max_length=10, unique=True)

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, verbose_name=_('groups'))
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, verbose_name=_('user permissions'))

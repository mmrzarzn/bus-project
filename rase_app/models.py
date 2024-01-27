from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # email_active_code = models.CharField(max_length=100, verbose_name='code active email')
    # about_user = models.TextField(null=True, blank=True, verbose_name='about user')
    # address = models.TextField(null=True, blank=True, verbose_name='address')
    admin = models.BooleanField(verbose_name='is_admin', default=False)
    is_activ = models.BooleanField(verbose_name='is_active', default=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '' :
            return self.get_full_name()

        return self.email
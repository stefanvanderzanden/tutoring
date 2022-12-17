from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    name = models.CharField(max_length=100)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.name


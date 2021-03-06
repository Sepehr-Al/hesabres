from django.db import models
from django.utils.translation import gettext as _


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'),unique=True)
    price = models.IntegerField(verbose_name=_('Price'))

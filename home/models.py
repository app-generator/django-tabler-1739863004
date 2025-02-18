# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    merchant_id = models.TextField(max_length=255, null=True, blank=True)
    bonus_id = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bonuses(models.Model):

    #__Bonuses_FIELDS__
    url = models.TextField(max_length=255, null=True, blank=True)
    merchantname = models.TextField(max_length=255, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    transactiontype = models.TextField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    minwithdraw = models.IntegerField(null=True, blank=True)
    maxwithdraw = models.IntegerField(null=True, blank=True)
    rollover = models.IntegerField(null=True, blank=True)
    claimconfig = models.TextField(max_length=255, null=True, blank=True)
    merchant_id = models.TextField(max_length=255, null=True, blank=True)

    #__Bonuses_FIELDS__END

    class Meta:
        verbose_name        = _("Bonuses")
        verbose_name_plural = _("Bonuses")


class Merchants(models.Model):

    #__Merchants_FIELDS__
    merchant_id = models.ForeignKey(Bonuses, on_delete=models.CASCADE)
    merchantname = models.TextField(max_length=255, null=True, blank=True)

    #__Merchants_FIELDS__END

    class Meta:
        verbose_name        = _("Merchants")
        verbose_name_plural = _("Merchants")



#__MODELS__END

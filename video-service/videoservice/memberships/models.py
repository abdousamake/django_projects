# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField()
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=40)

    def __srt__(self):
        return self.membership_type
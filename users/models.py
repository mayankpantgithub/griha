# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class GrihaUser(models.Model):

    full_name = models.TextField()

    phone = models.TextField()

    names = ArrayField(models.TextField()) # list of individual parts

    dob = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)



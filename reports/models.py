# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


INCIDENT_CHOICES = (
        ('erosion', 'Erosion'),
        ('discharge', 'Illicit Discharge'),
    )

class Report(models.Model):
    user = models.ForeignKey(User)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    incident_type = models.CharField(choices=INCIDENT_CHOICES, max_length=20)
    details = models.TextField(blank=True, null=True)
    picture = models.FileField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

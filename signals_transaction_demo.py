# -*- coding: utf-8 -*-
"""Untitled35.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13GXfGj8tcrFHSrqI4s2bKUO97_ywNqV9
"""

# Answer: Django signals run in the same database transaction as the caller.

from django.db import models, connection
from django.db.models.signals import post_save
from django.dispatch import receiver

class SampleModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SampleModel)
def transaction_check(sender, instance, **kwargs):
    print(f"Inside signal, autocommit: {connection.get_autocommit()}")
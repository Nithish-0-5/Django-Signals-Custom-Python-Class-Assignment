# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MXtbYSpfFi50-WGzUdA0oiYYsRFUxhZi
"""

# Answer: Django signals are synchronous by default.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")

User.objects.create(username="testuser")
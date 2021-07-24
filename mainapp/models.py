from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Program', 'Program'),
        ('Game', 'Game'),
        ('Etc', 'Etc'),
    ]
    PAY_CHOICES = [
        ('month', 'month'),
        ('quarter', 'quarter'),
        ('half', 'half'),
        ('yearly', 'yearly'),
    ]
    SHARED_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    category = models.CharField(
        max_length=100, default='Entertainment', choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100, help_text='원')
    pay_interval = models.CharField(
        max_length=100, default='month', choices=PAY_CHOICES)
    shared = models.CharField(
        max_length=100, default='1', choices=SHARED_CHOICES)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name

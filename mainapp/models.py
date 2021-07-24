from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('OTT', 'OTT'),
        ('Music', 'Music'),
        ('Shopping', 'Shopping'),
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
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100, help_text='원')
    pay_interval = models.CharField(max_length=100, choices=PAY_CHOICES)
    shared = models.CharField(max_length=100, choices=SHARED_CHOICES)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name

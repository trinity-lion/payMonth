from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "category", "cost",
                  'pay_interval', 'shared', 'image']

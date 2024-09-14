from django import forms
from . import models


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscribe
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w3-input w3-border',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w3-input w3-border',
                'placeholder': 'Enter e-mail'
            })
        }



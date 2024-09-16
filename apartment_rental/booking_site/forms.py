from django import forms
from . import models
from django.contrib.auth.models import User

# class SubscribeForm(forms.ModelForm):
#     class Meta:
#         model = models.Subscribe
#         fields = ['name', 'email']
#         widgets = {
#             'name': forms.Input(attrs={
#                 'class': 'w3-input w3-border',
#                 'placeholder': 'Enter name'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'w3-input w3-border',
#                 'placeholder': 'Enter e-mail'
#             })
#         }
        
class SearchAvailabilityForm(forms.ModelForm):
    class Meta:
        model = models.SearchAvailability
        fields = ['check_in', 'check_out','adults','kids']
        widgets = {
            'check_in': forms.DateInput(attrs={
                'class': 'w3-input w3-border',
                'placeholder': 'DD MM YY',
                'type':'date'
            }),
            'check_out': forms.DateInput(attrs={
                'class': 'w3-input w3-border',
                'placeholder': 'DD MM YY',
                'type':'date'
            }),
            'adults': forms.NumberInput(attrs={
                'class': 'w3-input w3-border'
            }),
            'kids': forms.NumberInput(attrs={
                'class': 'w3-input w3-border'})
            }
                


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = models.UserProfileInfo
        fields = ('portfolio_site','profile_pic')
from django import forms
from django.contrib.auth.models import User
from .models import Customer
class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class AttributesCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('avatar',)

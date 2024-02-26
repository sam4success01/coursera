from django import forms

from django.forms.widgets import NumberInput

from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'


class DemoForm(forms.Form):
    name=forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    email=forms.EmailField(label="Enter email address")
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

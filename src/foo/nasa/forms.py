from django import forms
from django.forms import ModelForm
from .models import PhotoOfDay

from bootstrap_datepicker_plus import DatePickerInput
from django import forms

class PhotoOfDayForm(forms.Form):
    # photodate = forms.DateField()
    photodate = forms.DateField(
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    title = forms.CharField()
    url = forms.CharField()
    hdurl = forms.CharField()
    copyright = forms.CharField()
    explanation = forms.CharField(widget=forms.Textarea)
    media_type = forms.CharField()
    service_version = forms.CharField()

from django.forms import ClearableFileInput, ModelForm
from .models import Cleaning

class CleaningForm(ModelForm):
  class Meta:
    model = Cleaning
    fields = ['day', 'month']


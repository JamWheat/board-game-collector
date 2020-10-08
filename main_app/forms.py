from django import forms
from django.forms import ModelForm
from .models import Play

class DateInput(forms.DateInput):
    input_type = 'date'

class PlayForm(ModelForm):
  class Meta:
    model = Play
    fields = ['date', 'num_players', 'rating']
    widgets = { 'date': DateInput() }
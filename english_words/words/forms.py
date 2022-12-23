from django import forms
from .models import Words


class AddWordForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['name', 'category_id']

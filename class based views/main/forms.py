from django import forms
from main.models import Style

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = ('text','image')
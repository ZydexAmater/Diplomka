from django import forms
from .models import NurseVisit

class NurseVisitForm(forms.ModelForm):
    class Meta:
        model = NurseVisit
        fields = ['name', 'group', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Аты-жөні'}),
            'group': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Тобы'}),
            'reason': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Себебін жазыңыз...', 'rows': 3}),
        }
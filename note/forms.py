from core.models import Note
from django import forms

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('memo', 'images','important')
        widgets= {
            'important': forms.CheckboxInput
        }

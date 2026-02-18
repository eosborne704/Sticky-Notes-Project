"""
Creating the form for user
to write and edit notes
"""
from django import forms
from .models import Note

class NotesForm(forms.ModelForm):
    """
    Form for writing and editing notes
    """
    class Meta:
        """
        Fields for writing and editing
        """
        model = Note
        fields = ["title", "content", "user"]


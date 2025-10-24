from django import forms
from .models import KnowledgeEntry

class KnowledgeEntryForm(forms.ModelForm):
    class Meta:
        model = KnowledgeEntry
        fields = ['title', 'content', 'tags', 'attachment']

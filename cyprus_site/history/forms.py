from django import forms

from history.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Text',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

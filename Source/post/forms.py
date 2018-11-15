from django import forms
from .models import Post
from froala_editor.widgets import FroalaEditor


class ProfileForm(forms.ModelForm):
    body = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'body', 'date')

from django import forms
from .models import Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('author_name', 'title', 'poetry_text',)
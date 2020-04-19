from django import forms

from .models import Article

class ArticleParseRequestForm(forms.ModelForm):

    url = forms.URLField(label='url', max_length=200)
    class Meta:
        model = Article
        fields = ('url',)
from django import forms
from django.utils.translation import ugettext_lazy

from .models import Article

# class URLField2(forms.URLField):
#     default_error_messages = {
#         'required': ugettext_lazy('Пожалуйста заполните поле'),
#         'invalid': ugettext_lazy('Пожалуйста введите URL'),
#     }


class ArticleParseRequestForm(forms.ModelForm):
    source = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'новостное издание'}))
    text = forms.CharField(label='text', max_length=3000,widget=forms.TextInput(attrs={'placeholder': 'текст статьи'}))
    class Meta:
        model = Article
        fields = ('source','text',)
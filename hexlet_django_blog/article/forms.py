from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ArticleComment, Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий') # Текст комментария

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
        labels = {
            'name': _("Название"),
            'body': _("Краткое описание"), 
        }
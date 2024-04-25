from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CommentArticleForm, ArticleForm
from .models import Article

from hexlet_django_blog.article.models import Article

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 
                      'articles/show.html', 
                      context={'article': article,}
                     )

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 
                      'articles/index.html', 
                      context={'articles': articles,}
                     )

class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form}) # Передаем нашу форму в контексте
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данные формы на корректность
            comment = Comment(
                name = form.cleaned_data['content'], # Получаем очищенные данные из поля content
                        # Заполняем оставшиеся поля
                )
            comment.save()

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Новая книга успешно добавлена!")
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={'form': form, 'article_id': article_id})
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f"Книга {form.cleaned_data['name']} успешно изменена!")
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            messages.add_message(request, messages.SUCCESS, f"Книга {article.name} успешно удалена!")
            article.delete()
        return redirect('articles')

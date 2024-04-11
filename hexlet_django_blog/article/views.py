from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View

class ArticlesView(View):

    tags = 'python'
    article_id = 42

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse("article", args=(self.tags, self.article_id)))

class Article(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Статья номер " + str(self.kwargs['article_id']) + ". Тег " + self.kwargs['tags'])

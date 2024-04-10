from django.views.generic.base import View
from django.shortcuts import render

class ArticlesView(View):

    app_name = "articles"

    def get(self, request, *args, **kwargs):
        return render(request, "articles/index.html", context={"name": self.app_name})

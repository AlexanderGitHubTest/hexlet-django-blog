from django.shortcuts import render

def index(request):
    app_name = "articles"
    return render(request, "articles/index.html", context={"name": app_name})

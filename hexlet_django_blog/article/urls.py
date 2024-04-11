from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [path('', views.ArticlesView.as_view()),
               path('<str:tags>/<int:article_id>/', views.Article.as_view(), name='article'),
              ]
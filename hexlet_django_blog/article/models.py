from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField()               # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=200) # текст комментария

    def __str__(self):
        return self.name

class ArticleComment(models.Model):
    content = models.CharField('content', max_length=100)

    def __str__(self):
        return self.name

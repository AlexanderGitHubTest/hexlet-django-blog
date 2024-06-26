from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')  # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),) # Перечисляем поля для фильтрации

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Перечисляем поля, отображаемые в таблице списка статей


from django.contrib import admin
from articles.models import Article, Comment, Genre, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rate', 'publication_date', 'count_like', 'count_dislike')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'count_like', 'count_dislike')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

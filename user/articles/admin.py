from django.contrib import admin

from . import models


class CommentInline(admin.TabularInline):
    model = models.Coment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Coment)

from django.contrib import admin
from .models import AuthorModel, ArticleModel
# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(ArticleModel)
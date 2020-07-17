from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name  = models.CharField(max_length = 100)
    email = models.EmailField()

class ArticleModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey('AuthorModel', on_delete=models.CASCADE, related_name ='articles')
    

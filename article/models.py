from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.SET_NULL)
    title = 


class Comment(models.Model):
    """주석"""
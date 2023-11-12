from django.urls import path
from article import views

urlpatterns = [
    path("comment/<pk>", views.CommentView.as_view()),
    path("<username>/<pk>/comment", views.ArticleView.as_view()),
    path("<username>/<pk>", views.ArticleView.as_view()),
    path("<username>/", views.ArticleView.as_view()),
    path("", views.ArticleView.as_view()),
]
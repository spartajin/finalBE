from django.urls import path
from user import views

urlpatterns = [
    path("login", views.UserLoginView.as_view()),
    path("logout", views.UserLogoutView.as_view()),
    path("article", views.UserArticleView.as_view()),
    path("", views.UserView.as_view()),
]
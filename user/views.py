from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class UserLoginView(APIView):
    def post(self, request):
        """로그인"""

class UserLogoutView(APIView):
    def post(self, request):
        """로그아웃"""

class UserArticleView(APIView):
    def get(self, request):
        """게시글 목록 리스폰스"""

class UserCommentView(APIView):
    def get(self, request):
        """댓글목록""" 


class UserView(APIView):
    def get(self, request):
        """유저정보 리스폰스"""

    def post(self, request):
        """사용자정보 받아 회원가입"""


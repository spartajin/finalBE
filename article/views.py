from rest_framework.views import APIView
# Create your views here.

class ArticleView(APIView):
    def get(self, request, username, pk=None):
        """게시글 본다 피케이 없으면 목록"""
    def post(self, request):
        """게시글 작성"""
    def put(self, request, pk):
        """지정된 게시글을 수정"""
    def delete(self, request, pk):
        """지정된 게시글 삭제"""

class CommentView(APIView):
    def post(self, request, article_id):
        """코멘트 작성"""
    def put(self, request, pk):
        """지정된 댓글 수정"""
    def delete(self, request, pk):
        """지정된 댓글 삭제"""
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


# Create your views here.

# class TestAPIView(APIView):
#
#     def get(self, request, format=None):
#         return Response({'message': 'Hello, World!'})


class BlogListView(generics.ListAPIView):
    """
    List all the blogs, posted by all the users.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = []

class BlogListDetail(generics.ListAPIView):
    """
    Retrieve s specific blog, posted by a specific user.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = []



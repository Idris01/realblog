from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post

# Create your views here.
class PostListView(generics.ListCreateAPIView):
    serializer_class=PostSerializer
    queryset=Post.postobjects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=PostSerializer
    queryset=Post.objects.all()



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category']

    def get_queryset(self):
        return Post.objects.prefetch_related('author').all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

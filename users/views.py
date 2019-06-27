from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from .models import CustomerUser, Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import isAuthOrReadOnly

# Create your views here.

class UserListView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [isAuthOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
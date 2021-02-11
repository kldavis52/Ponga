from rest_framework import views, viewsets, generics, status
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from api.serializers import VideoSerializer, CommentSerializer, UserSerializer
from core.models import Video, Comment
from users.models import User


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
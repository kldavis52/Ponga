from django.http.response import Http404
from rest_framework import views, viewsets, generics, status, mixins
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from api.serializers import VideoSerializer, CommentSerializer, UserSerializer
from core.models import Video, Comment
from users.models import User


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetailView(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    GET, POST, PATCH, PUT, DELETE a single video.
    """

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
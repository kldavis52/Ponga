from django.http.response import Http404
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


class VideoDetailView(views.APIView):
    """
    Retrieve, update or delete a video
    """

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk=pk)
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk=pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
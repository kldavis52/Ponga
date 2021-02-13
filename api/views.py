from django.http.response import Http404
from django.core.files import File

from rest_framework import views, viewsets, generics, status, mixins
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions

from api.serializers import VideoSerializer, CommentSerializer, UserSerializer
from core.models import Video, Comment
from users.models import User
from studiopal.settings import AZURE_STATIC_ROOT, MEDIA_ROOT

from moviepy.editor import *
from PIL import Image


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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

    parser_classes = [MultiPartParser, FormParser]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        def create_video_thumbnail(video_obj):
            video_path = os.path.join(MEDIA_ROOT, video_obj.video.name)
            with VideoFileClip(video_path, audio=False) as clip:
                max_duration = int(clip.duration) + 1
                print(max_duration)
                frame_at_second = 3
                thumbnail_frame = clip.get_frame(frame_at_second)
                video_thumbnail = Image.fromarray(thumbnail_frame)
                thumbnail_path = os.path.join(AZURE_STATIC_ROOT, f"{video}.jpg")
                video_thumbnail.save(thumbnail_path)

                # create an ImageFile compatable with Django's ORM/Postgres

                try:
                    thumbnail_buffer = open(thumbnail_path, "rb")
                except FileExistsError:
                    raise Exception("thumbnail file not captured from video properly")

                thumbnail = File(thumbnail_buffer)

                video.video_thumbnail.save(f"{video}.jpg", thumbnail)

        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            video = serializer.save(creator=request.user)
            serializer.save()
            create_video_thumbnail(video)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
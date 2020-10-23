from django import forms
from django.core.files import File
from django.core.files.storage import default_storage

from .models import Video, Comment, User
from moviepy.editor import *
from PIL import Image


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    video = forms.FileField(required=True, widget=forms.FileInput())
    video_thumbnail = forms.ImageField(widget=forms.HiddenInput())

    class Meta:
        model = Video
        fields = [
            "title",
            "description",
            "video",
            "video_thumbnail",
        ]

    def save(self):
        user = super(VideoForm, self).save()
        title = self.cleaned_data.get("title")
        description = self.cleaned_data.get("description")
        video = self.cleaned_data.get("video")

        video_thumbnail = create_thumbnail(user.video)

        def create_thumbnail(video_obj):
            with VideoFileClip(video_obj.path, audio=False) as clip:
                duration = clip.duration
                max_duration = int(clip.duration) + 1
                frame_at_second = 3
                thumbnail_clip = clip.get_frame(frame_at_second)
                clip.close()
                fh = default_storage.open(video_obj, "wb")
                video_thumbnail = Image.fromarray(thumbnail_clip)
                thumbnail_format = "jpg"
                video_thumbnail.save(fh, thumbnail_format)
                fh.close()
                video_thumbnail.save(video_obj.path)
                return video_thumbnail

        return user


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class InstructorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "studio_name",
            "profile_photo",
            "bio",
            "paypal_donation_url",
        ]

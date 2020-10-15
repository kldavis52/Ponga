from django import forms
from .models import Video, Comment, User


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "video",
        ]



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'

        ]


class InstructorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            # 'profile_photo',
            # 'image_medium',
            "bio",
        ]
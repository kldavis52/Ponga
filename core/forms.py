from django import forms
from .models import Video, Comment, User


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "video",
        ]


# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = [
#             #"user",
#             "creator",
#             "upvoted",
#             "image",
#             #"thumbnail",


#         ]


# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'text'
#             'author'
#             'pu_date'
#         ]


class InstructorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'profile_photo',
            "bio",
        ]
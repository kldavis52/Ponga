from django import forms
from .models import Video, Comment



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            #"user",
            "creator",
            "upvoted",
            "image",
            #"thumbnail",
            
            
            
        ]



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text'
            'author'
            'pu_date'
        ]

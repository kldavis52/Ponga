from rest_framework import serializers
from core.models import Video, Comment
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "studio_name",
            "profile_photo",
            "user_bio",
            "paypal_donation_url",
            "joined_date",
        ]


class VideoSerializer(serializers.ModelSerializer):
    video_thumbnail = serializers.ImageField(required=False)
    liked_by = serializers.PrimaryKeyRelatedField(many=True, queryset=User)
    creator = serializers.PrimaryKeyRelatedField(
        queryset=User, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Video
        fields = [
            "title",
            "description",
            "creator",
            "video",
            "video_thumbnail",
            "publish_date",
            "liked_by",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "text",
            "pub_date",
        ]

from rest_framework import serializers
from .models import SocialUserModel, PostModel, TagsPostModel, LikePostModel


class SocialUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUserModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsPostModel
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePostModel
        fields = '__all__'

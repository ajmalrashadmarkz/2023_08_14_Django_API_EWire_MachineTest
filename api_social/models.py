from django.db import models

# Create your models here.


class SocialUserModel(models.Model):
    name = models.CharField(max_length=54)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=54)
    username = models.CharField(unique=True, max_length=54)
    password = models.CharField(max_length=54)
    
    
    
class PostModel(models.Model):
    postId = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(SocialUserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=54)
    description = models.CharField(max_length=224, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    
class TagsPostModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    tagText = models.CharField(max_length=54)
    
class LikePostModel(models.Model):
    likeId = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(SocialUserModel, on_delete=models.CASCADE)
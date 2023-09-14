from django.contrib import admin
from post.models import Post, Tag, LikeOrUnlike

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(LikeOrUnlike)

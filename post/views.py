from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Post, LikeOrUnlike,Tag
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import PostForm,TagForm


# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_list.html"

    # def list_posts(request):
    #     posts = Post.objects.all()
    #     user_liked_posts = request.user.likeByUser.all().values_list("post", flat=True)
    #
    #     context = {"posts": posts, "user_liked_posts": user_liked_posts}
    #
    #     return render(request, "post_list.html", context)

class PostDetailView(LoginRequiredMixin, DetailView):  # new
    model = Post
    template_name = "post_detail.html"

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = (
        "title",
        "description",
        "tags",
    )


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tag_new.html"
    fields = (
        "title",
    )


# @login_required
# def like(request, post_id):
#     user = request.user
#     post = Post.objects.get(id=post_id)
#     current_likes = post.likes
#     liked = Likes.objects.filter(user=user, post=post).count()
#
#     if not liked:
#         Likes.objects.create(user=user, post=post)
#         current_likes = current_likes + 1
#     else:
#         Likes.objects.filter(user=user, post=post).delete()
#         current_likes = current_likes - 1
#
#     post.likes = current_likes
#     post.save()
#     # return HttpResponseRedirect(reverse('post-details', args=[post_id]))
#     return HttpResponseRedirect(reverse('post_list', args=[post_id]))

# def like(request, post_id):
#     post = Post.objects.get(pk=id)
#     user = User.objects.get(pk=request.user.id)
#     likePost = Likes(user=user, post=post)
#     likePost.save()
#     return JsonResponse({"message": "Liked"})

# def unlike(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     user = User.objects.get(pk=request.user.id)
#     unlikePost = LikeOrUnlike.objects.filter(user=user, post=post)
#     unlikePost.delete()
#     return JsonResponse({"message": "Unliked"})

# def like_or_unlike_fetch(request):
#     data = json.loads(request.body)
#     user_id = data.pop("user_id")
#     post_id = data.pop("post_id")
#
#     user = get_user_model().objects.get(pk=user_id)
#     post = Post.objects.get(pk=post_id)
#     data.update({"user": user, "post": post})
#
#     post = Likes.objects.filter(**data)
#     if not post:
#         Likes.objects.create(**data)
#         liked = True
#     else:
#         post.delete()
#         liked = False
#
#     return JsonResponse({"liked": liked})

def index(request):
    likes = LikeOrUnlike.objects.all()
    postLiked = []
    try:
        for like in likes:
            if like.user.id == request.user.id:
                postLiked.append(like.post.id)
    except:
        postLiked = []
    return render(request, "post_list.html", {
        'likes': likes,
        'postLiked': postLiked

    })  # function for liking post


def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    likePost = LikeOrUnlike(user=user, post=post)
    likePost.save()
    return JsonResponse({"message": "Liked"})


# function for unliking post
def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    unlikePost = LikeOrUnlike.objects.filter(user=user, post=post)
    unlikePost.delete()
    return JsonResponse({"message": "Unliked"})





from django.urls import path
from . import views

from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    TagCreateView,
)

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("", PostListView.as_view(), name="post_list"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("tag/new", TagCreateView.as_view(), name="tag_new"),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/unlike/', views.unlike, name='unlike'),
]
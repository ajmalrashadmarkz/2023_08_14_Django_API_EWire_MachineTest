from django.urls import path

from .views import SocialUserCreate, SocialUserLogin, CreatePostView, LikePostView
urlpatterns = [

  path('register/user', SocialUserCreate.as_view()),
  
  path('user/login', SocialUserLogin.as_view()),
  
  path('create/post/publish', CreatePostView.as_view()),
  path('create/post/unpublish/<int:pk>', CreatePostView.as_view()),
   path('list/posts/all', CreatePostView.as_view()),
   path('like/like', LikePostView.as_view()),
   path('list/unlike/<int:pk>', LikePostView.as_view()),
  

  
  
  


]
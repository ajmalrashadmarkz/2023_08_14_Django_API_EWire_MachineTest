from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializer import SocialUserModelSerializer, PostSerializer, LikeSerializer
from .models import SocialUserModel, PostModel, LikePostModel


class SocialUserCreate(APIView):
    def post(self, request):
        data = request.data
        serializer = SocialUserModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class SocialUserLogin(APIView):
    def post(self, request):
        data = request.data
        print(data)
        user = SocialUserModel.objects.filter(username=data['username']).exists()

        # user = authenticate(username = serializer.data['username'], password = serializer.data['password'])

        if user is False:
            return Response({

                'user does not exist'
            }, status.HTTP_400_BAD_REQUEST)

        user = SocialUserModel.objects.get(username=data['username'])
        if user.username == data['username'] and user.password == data['password']:

            return Response({'user_login': 'succus', 'userId': user.pk})

        else:
            return Response({'check your password'})


class CreatePostView(APIView):
    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk):
        post_delete = PostModel.objects.get(postId=pk).delete()
        return Response('succusfully deleted')

    def get(self, request):
        post_all = PostModel.objects.all()
        serializer = PostSerializer(post_all, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    def post(self, request):
        data = request.data
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, requst, pk):
        dislike = LikePostModel.objects.get(likeId=pk).delete()
        return Response({'succusfull deleted'})



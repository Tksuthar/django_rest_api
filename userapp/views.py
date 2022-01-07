from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .serializers import UserSerializer
from .models import UserModel



class UserList(APIView):
    def get(self, request, pk=None, format=None):
        if pk is None:
            users = UserModel.objects.all()
            query = self.request.GET.get('search')

            if query is not None:
                users = users.filter(user_lname=query) | users.filter(user_fname=query)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def post(self, request, pk=None, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        user = UserModel.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        user = UserModel.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partially Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        user = UserModel.objects.get(pk=id)
        user.delete()

        return Response({'msg': 'User deleted'})

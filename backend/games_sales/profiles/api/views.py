from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import Account
from ..models import Profile
from .serializers import ProfileSerializer


class ProfileDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        try:
            user = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        profile = user.profile
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        try:
            user = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        profile = user.profile
        serializer = ProfileSerializer(profile, request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, username, format=None):
        data = {}

        try:
            user = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        profile = user.profile
        profile.delete()

        data['response'] = f'User ${username} has successfully been deleted.'
        return Response(data, status=status.HTTP_204_NO_CONTENT)

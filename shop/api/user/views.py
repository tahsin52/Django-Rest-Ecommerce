from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import permissions
from .permissions import UptadeOwnUser
from .models import User, Profile, Adress
from .serializers import UserSerializer, ProfileSerializer, AdressSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UptadeOwnUser,)

    def perform_create(self, serializer):
        serializer.save()
        print(serializer.data)


class LoginView(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    authentication_classes = (TokenAuthentication,)



    def create(self, request):
        return ObtainAuthToken().post(request)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated)
    serializer_class = ProfileSerializer

    def list(self, request):
        profile = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(profile[0])
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdressView(viewsets.ModelViewSet):
    queryset = Adress.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = AdressSerializer
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

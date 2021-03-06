from users.models import Profile
from users.serializers import ProfileSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    print ">>>>>>>>>>>>"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
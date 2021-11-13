from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets 
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerialize, GroupSerializer

# Create your views here.
class UserViewSet (viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerialize
    permission_class = [permissions.IsAuthenticated]

class GroupViewSet(viewset.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.isAuthenticated]
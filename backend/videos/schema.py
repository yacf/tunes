import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout

from videos.models import Videos

class VideosType(DjangoObjectType):
    class Meta:
        model = Videos

class Query(graphene.ObjectType):
    videos = graphene.List(VideosType)
    
    def resolve_videos(self, info, **kwargs):
        return Videos.objects.all()
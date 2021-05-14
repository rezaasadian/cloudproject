from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from .models import Doctor, VisitTime
from .serializers import *
from .permissions import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_user(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny, ))
class DoctorViewSet_user(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    http_method_names = ['get']
    search_fields = ('name', )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'degree', 'specialty']

    ordering_fields = '__all__'

@permission_classes((IsAuthenticated, IsAdmin))
class DoctorViewSet_admin(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'


class VisitTimeViewSet_user(viewsets.ModelViewSet):
    queryset = VisitTime.objects.all()
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctor']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return VisitTimeSerializer
        else:
            return DoctorVisitTimeSerializer


@permission_classes((IsAuthenticated,IsAdmin))
class VisitTimeViewSet_admin(viewsets.ModelViewSet):
    queryset = VisitTime.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return VisitTimeSerializer
        else:
            return DoctorVisitTimeSerializer


@permission_classes((IsAuthenticated,IsAdmin))
class UserVisitTimeViewSet_admin(viewsets.ModelViewSet):
    queryset = UserVisit.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return UserVisitTimeSerializer
        else:
            return UserDoctorVisitTimeSerializer



@permission_classes((IsAuthenticated,))
class CommentOnDoctor_user(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','doctor']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CommentOnDoctorSerializer
        else:
            return UserCommentOnDoctorSerializer



@permission_classes((IsAuthenticated,))
class UserFavoriteViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']




@api_view(['GET'])
@permission_classes((IsAuthenticated, IsOwner))
def UserProfileViewSet(request):
    try:
        user = User.objects.get(username=request.query_params['username'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = UserSerializer(user)
    return Response(ser.data, status=status.HTTP_200_OK)



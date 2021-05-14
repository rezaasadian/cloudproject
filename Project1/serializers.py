from rest_framework import serializers
from .models import Doctor, VisitTime, Comment, UserVisit, UserFavorite
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorSerializer_small(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'specialty', 'degree', 'city')


class VisitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = '__all__'


class DoctorVisitTimeSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    class Meta:
        model = VisitTime
        fields = '__all__'
        # depth = 1

class UserVisitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVisit
        fields = '__all__'
        # depth = 1

class UserDoctorVisitTimeSerializer(serializers.ModelSerializer):
    visittime = DoctorVisitTimeSerializer()
    user = User
    class Meta:
        model = UserVisit
        fields = '__all__'
        #depth = 1

class CommentOnDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class UserCommentOnDoctorSerializer(serializers.ModelSerializer):
    doctor =    DoctorSerializer_small()
    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1

class UserFavoriteSerializer(serializers.ModelSerializer):
    #doctor = DoctorSerializer_small()
    class Meta:
        model = UserFavorite
        fields = '__all__'
        #depth = 1
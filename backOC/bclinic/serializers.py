from rest_framework import serializers
from .models import Demo, User
class DemSerializer(serializers.ModelSerializer):
     class Meta:
         model = Demo
         fields = ('id','mail', 'password')
    # mail=serializers.EmailField(max_length=100)
    # password=serializers.CharField(max_length=40)
    # def create(self, validated_data):
    #     return super().create(validated_data)
class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model=User
          fields=('id', 'fname', 'lname', 'email', 'password')
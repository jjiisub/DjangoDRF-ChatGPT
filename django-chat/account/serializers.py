from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드는 응답에 포함되지 않도록 설정

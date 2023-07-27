from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from rest_framework.views import APIView


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'state': True, 'message': '회원가입이 성공적으로 완료되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response({'state': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.get(user=user)
            print(user, token)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': '유효하지 않은 인증 정보입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    



class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        # 클라이언트에서 전달한 토큰 값을 가져옵니다.
        token = request.data.get('token')

        if token:
            try:
                # 토큰 값으로 해당 토큰을 가진 유저를 찾습니다.
                token = Token.objects.get(key=token)
                user = token.user
                # 해당 토큰을 삭제하여 로그아웃 처리합니다.
                token.delete()
                return Response({'message': f'{user.username}님, 로그아웃되었습니다.'}, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return Response({'message': '유효하지 않은 토큰입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': '토큰이 전달되지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import LoginSerializer, UserSerializer, UserImageSerializer, LanguageSerializer
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MyUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            print(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
    
class ProfileImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MyUser.objects.all()
    serializer_class = UserImageSerializer

    @action(detail=False, methods=['get'], url_path='me')
    def get_current_user_image(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    

class LanguageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LanguageSerializer(data = request.data)
        if serializer.is_valid():
            user = request.user
            language = serializer.validated_data.get('language')
            user.language = language
            user.save()
            print('language change')
            return Response({"language": UserSerializer(request.user).data.get("language")})

    def get(self, request):
        return Response({"language": UserSerializer(request.user).data.get("language")})

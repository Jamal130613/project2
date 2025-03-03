from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from applications.account.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            message = f'You are successfully registered.We send you activation code.'
            return Response(message, status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Success'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Code is not correct!'}, status=400)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

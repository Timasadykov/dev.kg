from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password


from django.contrib.auth import get_user_model


from django.contrib.auth import get_user_model

User = get_user_model()


from apps.company.serializers import (CompanySerializer)
from apps.company.models import Company


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

# class RegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data

#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')

#         if User.objects.filter(username = username). exists():
#             return Response({"message": 'User with such username is already  exists'})

#         user = User.objects.create_user(
#             username=username,
#             email= email,
#             password=password
#         )

        

#         token = Token.objects.create(user=user)
#         return Response({"token: token.key"})
    

# class AuthorizarionView(APIView):
#      def post(self, request):
#         serializer =AuthorizarionSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data

#         username = data.get('username')
#         password = data.get('password')

#         user  = User.objects.filter(username=username).first()

#         if user is not None:
#             if check_password(password, user.password):
#                 token, _ =Token.objects.get_or_create(user=user)
#                 return Response({"token": token.key})
#             return Response ({"error": 'Password is not valid'}, status=400)
#         return Response({'error':'this username is not resigtreted'}, status=400)






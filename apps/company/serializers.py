from rest_framework import serializers, exceptions

from apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id', 
            'name', 'logo', 'description','telegram', 'whatsapp',
            'vacanci_amount','event_amount','video_amount',
        )

# class RegistrationSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     email = serializers.CharField()


#     def validate_password (self, value):
#         if len(value) < 8:
#             raise exceptions.ValidationError('Password is too short ')
#         elif len(value) >  24:
#             raise exceptions.ValidationError("Password is too long")
#         return value


# class AuthorizarionSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()


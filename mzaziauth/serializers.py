import enum
from django.contrib.auth import authenticate
from django.forms import ValidationError
from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Profile
        fields = ('user', 'prof_pic', 'bio')


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class UserRoles(enum.Enum):
        SingleParent = 'SingleParent'
        Counsellor = 'Counsellor'
        def __str__(self):
            return self.value
    
    profile = ProfileSerializer(read_only=True)
    roles = [role.value for role in UserRoles]
    user_role = serializers.ChoiceField(choices=roles,required=True)
    # user_role = serializers.SlugRelatedField(slug_field=UserRoles.user_role,queryset=UserRoles.objects.all())
    class Meta:
        model = CustomUser
    
        fields = ['email', 'username', 'f_name','l_name','profile','user_role','password']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        if not email and not password:
            resp = {
                "email": 'Enter a valid email',
                "password": 'Enter a valid password'
                }
            raise serializers.ValidationError(resp)
        LoggedInCustomUser = authenticate(username=email, password=password)
        
        if LoggedInCustomUser is None:
            resp = {
                "error": 'Invalid username or password'
                 }
            raise serializers.ValidationError(resp)
        if not LoggedInCustomUser.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "email":LoggedInCustomUser.email,
            "username":LoggedInCustomUser.username,
            'token': LoggedInCustomUser.token,
        }
        
#SERIALIZER FOR A LIST OF ALL UserS
class UserListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Profile
        fields = '__all__'


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    # def save(self, **kwargs):

    #     try:
    #         RefreshToken(self.token).blacklist()

    #     except TokenError:
    #         self.fail('bad_token')
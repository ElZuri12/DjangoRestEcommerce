from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

"""     # - Como funciona un serializer 
    class TestUserSerializer(serializers.Serializer):
        name = serializers.CharField(max_length = 200)
        email = serializers.EmailField()
        
        def validate_name(self, value):
            # - Custom Validation
            if 'develop' is value:
                raise serializers.ValidationError('Error, no puede existir un usuario con ese name')
        
            return value
        
        def validate_email(self, value):
            # - Custom Validation
            if value == '':
                raise serializers.ValidationError('Tiene que indicar un correo')
            return value
        
        def validate(self, data):
            if data['name'] in data['email']:
                raise serializers.ValidationError('El email no puede contener el nombre')
            return data """
from core.models import User, PermissionGroup, Company
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'company']
    
    def update(self, instance, validated_data):
        instance.secret_identity = validated_data.get('your field name', 'defaultvalue')
        instance.save()
        return instance

class PermissionGroupSerializer(ModelSerializer):
    class Meta:
        model = PermissionGroup
        fields = ['group_name', 'permission_description', 'resource_name',
                  'access_level', 'username', 'company_name']

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']
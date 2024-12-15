from apps.agents.models import Token, SkillTemplate, Skill, Agent
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Token
        fields = '__all__'

def get_endpoints(raw_api_spec):
    endpoints = [
        {"endpoint":route, "type":operation}
        for route, operations in raw_api_spec["paths"].items()
        for operation in operations
        if operation in ["get", "post"]
    ]
    return endpoints

class SkillTemplateSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    endpoints = serializers.SerializerMethodField()

    def get_endpoints(self, obj):
        import yaml
        raw_api_spec = yaml.load(obj.openapi_schema, Loader=yaml.Loader)
        return get_endpoints(raw_api_spec)

    class Meta:
        model = SkillTemplate
        fields = '__all__'

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Skill
        fields = '__all__'

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    skills = SkillSerializer(read_only=True, many=True)
    
    class Meta:
        model = Agent
        fields = '__all__'




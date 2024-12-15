from apps.agents.models import Token, TokenConfig, Skill, ActiveSkill, Agent, AgentSkill
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = ['username']

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Token
        fields = '__all__'

class TokenConfigSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = TokenConfig
        fields = '__all__'

def get_endpoints(raw_api_spec):
    endpoints = [
        {"endpoint":route, "type":operation}
        for route, operations in raw_api_spec["paths"].items()
        for operation in operations
        if operation in ["get", "post"]
    ]
    return endpoints

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    endpoints = serializers.SerializerMethodField()
    token_config = TokenConfigSerializer(read_only=True)

    def get_endpoints(self, obj):
        import yaml
        raw_api_spec = yaml.load(obj.openapi_schema, Loader=yaml.Loader)
        return get_endpoints(raw_api_spec)

    class Meta:
        model = Skill
        fields = '__all__'

class ActiveSkillSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = ActiveSkill
        fields = '__all__'

class AgentSkillSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    skill = ActiveSkillSerializer(read_only=True)
    
    class Meta:
        model = AgentSkill
        fields = '__all__'

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    skills = AgentSkillSerializer(source='agentskill_set', many=True, read_only=True)
    
    class Meta:
        model = Agent
        fields = '__all__'




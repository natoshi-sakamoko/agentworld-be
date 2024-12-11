from apps.agents.models import Token, TokenConfig, Skill, ActiveSkill, Agent, AgentSkill
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ['name', 'description', 'value']

class TokenConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TokenConfig
        fields = '__all__'

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ActiveSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveSkill
        fields = '__all__'

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class AgentSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgentSkill
        fields = '__all__'


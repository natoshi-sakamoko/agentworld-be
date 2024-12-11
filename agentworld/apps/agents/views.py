from apps.agents.serializers import *
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TokenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticated]

class TokenConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows token_configs to be viewed or edited.
    """
    queryset = TokenConfig.objects.all().order_by('id')
    serializer_class = TokenConfigSerializer
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActiveSkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = ActiveSkill.objects.all()
    serializer_class = ActiveSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgentSkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = AgentSkill.objects.all()
    serializer_class = AgentSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

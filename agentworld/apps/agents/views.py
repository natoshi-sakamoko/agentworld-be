from apps.agents.serializers import *
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.agents.models import Skill, ActiveSkill
from apps.agents.serializers import ActiveSkillSerializer
from django.urls import path


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

class CreateActiveSkillFromTemplateView(APIView):
    """
    API endpoint that creates an ActiveSkill from a Skill template.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, skill_id):
        # Get the skill template
        skill = get_object_or_404(Skill, id=skill_id)
        # Get the token id
        token_id = request.data.get('token_id', None)
        if token_id is None:
            return Response({"error": "token_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        token = get_object_or_404(Token, id=token_id)
        
        # Create ActiveSkill with data from the skill template
        active_skill = ActiveSkill.objects.create(
            name=skill.name,
            description=skill.description,
            openapi_schema=skill.openapi_schema,
            guidelines=skill.guidelines,
            token_config=skill.token_config,
            token=token,
            creator=request.user,
            skill=skill  # Reference to the template
        )

        # Serialize and return the created ActiveSkill
        serializer = ActiveSkillSerializer(active_skill, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

from apps.agents.serializers import *
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.agents.models import Skill


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

class SkillTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = SkillTemplate.objects.all()
    serializer_class = SkillTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tokens to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateSkillFromTemplateView(APIView):
    """
    API endpoint that creates an Skill from a Skill template.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, skill_template_id):
        # Get the skill template
        skill_template = get_object_or_404(SkillTemplate, id=skill_template_id)
        # Get the token id
        token_id = request.data.get('token_id', None)
        if token_id is None:
            return Response({"error": "token_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        token = get_object_or_404(Token, id=token_id)
        
        # Create Skill with data from the skill template
        skill = Skill.objects.create(
            name=skill_template.name,
            description=skill_template.description,
            openapi_schema=skill_template.openapi_schema,
            guidelines=skill_template.guidelines,
            auth_header=skill_template.auth_header,
            auth_prefix=skill_template.auth_prefix,
            auth_headers=skill_template.auth_headers,
            token=token,
            creator=request.user,
            skill_template=skill_template  # Reference to the template
        )

        # Serialize and return the created Skill
        serializer = SkillSerializer(skill, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateAgentView(APIView):
    """
    API endpoint that creates an Agent from a POST request.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Get the data from request
        data = request.data.copy()

        # Get the skills IDs from the request
        skills_ids = data.pop('skills', [])
        
        # Create serializer with the data
        serializer = AgentSerializer(data=data, context={'request': request})
        
        if serializer.is_valid():
            # Save the agent
            agent = serializer.save(creator=request.user)
            
            # Add skills to the agent
            for skill_id in skills_ids:
                skill = get_object_or_404(Skill, id=skill_id)
                agent.skills.add(skill)
            
            # Re-serialize with the skills included
            serializer = AgentSerializer(agent, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

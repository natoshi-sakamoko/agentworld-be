from django.urls import include, path
from rest_framework import routers

from apps.agents import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tokens', views.TokenViewSet)
router.register(r'skill_templates', views.SkillTemplateViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'agents', views.AgentViewSet)

urlpatterns = [
    path('api/skill_templates/<uuid:skill_template_id>/create_skill/', views.CreateSkillFromTemplateView.as_view(), name='create-skill'),
    path('api/agents/~create/', views.CreateAgentView.as_view(), name='create-agent'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
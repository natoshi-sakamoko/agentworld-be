from django.urls import include, path
from rest_framework import routers

from apps.agents import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tokens', views.TokenViewSet)
router.register(r'token_configs', views.TokenConfigViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'active_skills', views.ActiveSkillViewSet)
router.register(r'agents', views.AgentViewSet)
router.register(r'agent_skills', views.AgentSkillViewSet)

urlpatterns = [
    path('api/skills/<uuid:skill_id>/activate/', views.CreateActiveSkillFromTemplateView.as_view(), name='create-active-skill'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
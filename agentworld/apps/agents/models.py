import uuid
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True, null=False, default="")
    description = models.CharField(max_length=500, blank=True, null=False, default="")
    value = models.CharField(max_length=500, blank=True, null=False, default="")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class TokenConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField(max_length=40, blank=True, null=False, default="")
    prefix = models.CharField(max_length=40, blank=True, null=False, default="")
    headers = models.JSONField(null=False, blank=True, default=dict)

def createTokenConfig():
    return TokenConfig(header="Authorization", prefix="Bearer")

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True, null=False, default="")
    description = models.CharField(max_length=500, blank=True, null=False, default="")
    icon = ProcessedImageField(upload_to='skill_icons/',
                             processors=[ResizeToFit(300, 300)],
                             format='JPEG',
                             options={'quality': 85},
                             blank=True,
                             null=True)
    openapi_schema = models.TextField()
    guidelines = models.JSONField(null=False, blank=True, default=list)
    token_config = models.ForeignKey(TokenConfig, null=True, blank=True, on_delete=models.PROTECT, default=createTokenConfig)
    category = models.CharField(
        max_length=50,
        choices=[
            ('AnalyticsAutomation', 'Analytics Automation'),
            ('ConversationManagement', 'Conversation Management'),
            ('CRM', 'CRM'),
            ('DataEnrichment', 'Data & Enrichment'),
            ('IssueTracking', 'Issue Tracking & Ticketing'),
            ('LeadCapture', 'Lead Capture'),
            ('MarketingAutomation', 'Marketing Automation'),
            ('PhoneVideo', 'Phone & Video'),
            ('Scheduling', 'Scheduling'),
            ('ScreenCapture', 'Screen Capture'),
            ('SocialMedia', 'Social Media'),
            ('SurveysFeedback', 'Surveys & Feedback'),
        ],
        null=True,
        blank=True
    )

class ActiveSkill(models.Model):
    """
    ActiveSkill can be created from scratch, as well as from templates.
    Name, Description, OpenAPI_schema, Guidelines can be customized.
    They will be populated from template (skill object) during creation.
    Tokens can be deleted later. So null = True. Creator can be deleted too.
    TokenConfig is null because maybe there is not auth required.
    Skill is reference to the template (will be null when creating from scratch.)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True, null=False, default="")
    description = models.CharField(max_length=500, blank=True, null=False, default="")
    openapi_schema = models.TextField()
    guidelines = models.JSONField(null=False, blank=True, default=list)
    token = models.ForeignKey(Token, null=True, blank=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    token_config = models.ForeignKey(TokenConfig, null=True, blank=True, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, null=True, blank=False, on_delete=models.PROTECT)

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=True, null=False, default="")
    description = models.CharField(max_length=500, blank=True, null=False, default="")
    instructions = models.JSONField(null=False, blank=True, default=list)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class AgentSkill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent = models.ForeignKey(Agent, null=False, on_delete=models.CASCADE)
    skill = models.ForeignKey(ActiveSkill, null=False, on_delete=models.PROTECT)
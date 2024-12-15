from core.settings.base import *

DEBUG = True

if DEBUG:
    import mimetypes
    mimetypes.add_type("text/javascript", ".js", True)

# Add these settings for development
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True  # Only use this in development!
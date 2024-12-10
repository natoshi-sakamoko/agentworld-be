from core.settings.base import *

DEBUG = True

if DEBUG:
    import mimetypes
    mimetypes.add_type("text/javascript", ".js", True)
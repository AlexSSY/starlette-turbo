import os
from dotenv import load_dotenv

from .context_processors import default, manifest


CURRENT_DIR = os.path.dirname(__file__)


DEBUG = True
TEMPLATE_DIRS = [
    os.path.join(CURRENT_DIR, "templates"),
]
STATICFILES_DIR = os.path.join(CURRENT_DIR, "static")
CONTEXT_PROCESSORS = [
    default,
    manifest,
]

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
UNAUTHENTICATED_REDIRECT_URL = "/signin"
JS_MANIFEST_FILE = os.path.join(CURRENT_DIR, "static/js/.vite/manifest.json")

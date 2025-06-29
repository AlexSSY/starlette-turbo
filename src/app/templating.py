from starlette.templating import Jinja2Templates

from . import settings


templating = Jinja2Templates(
    settings.TEMPLATE_DIRS, context_processors=settings.CONTEXT_PROCESSORS
)

from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse

from . import settings, crud


class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        user_id = request.session.get("user_id")
        if user_id is not None:
            user = crud.get_user_by_id(int(user_id))
            if user is not None:
                request.state.user = user
        return await call_next(request)


middlewares = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    Middleware(AuthenticationMiddleware),
]


class AuthRequiredMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if not hasattr(request.state, "user"):
            return RedirectResponse(settings.UNAUTHENTICATED_REDIRECT_URL, 302)
        return await call_next(request)

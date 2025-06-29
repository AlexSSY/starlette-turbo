from starlette.routing import Route
from starlette.middleware import Middleware

from . import views
from .middlewares import AuthRequiredMiddleware


routes = [
    Route("/", views.index, name="index", middleware=[Middleware(AuthRequiredMiddleware)]),
    Route("/signup", views.signup, name="signup"),
    Route("/signup/", views.signup_create, methods=["POST"], name="signup_create"),
    Route("/signin", views.signin, name="signin"),
    Route("/signin/", views.signin_create, methods=["POST"], name="signin_create"),
    Route("/signout/", views.signout, methods=["POST"], name="signout")
]

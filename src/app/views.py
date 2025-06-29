from starlette.requests import Request
from starlette.responses import RedirectResponse

from .templating import templating
from .crud import create_user, authenticate_user


def index(request: Request):
    return templating.TemplateResponse(request, "index.html")


def signup(request: Request):
    return templating.TemplateResponse(request, "auth/signup.html")
    

async def signup_create(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")
    password_confirmation = form_data.get("password_confirmation")
    
    errors = {}

    normalized_username = username.strip()
    if len(normalized_username) < 1:
        errors["username"] = "can't be empty"

    if len(password) < 5:
        errors["password"] = "length must be greater than 5"

    if password != password_confirmation:
        errors["password_confirmation"] = "passwords not match."

    if errors:
        return templating.TemplateResponse(request, "auth/signup.html", {"errors": errors}, status_code=400)

    create_user(username, password)
    return RedirectResponse(request.url_for("index"), status_code=302)


def signin(request: Request):
    return templating.TemplateResponse(request, "auth/signin.html")


async def signin_create(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    errors = {}

    normalized_username = username.strip()
    if len(normalized_username) < 1:
        errors["username"] = "can't be empty"

    user = authenticate_user(username, password)

    if user is None:
        errors["username"] = errors["password"] = "invalid credentials"

    if errors:
        return templating.TemplateResponse(request, "auth/signin.html", {"errors": errors}, 400)

    request.session["user_id"] = user.id
    return RedirectResponse(request.url_for("index"), status_code=302)


def signout(request: Request):
    request.session.pop("user_id")
    return RedirectResponse(request.url_for("index"), status_code=302)


def profile(request: Request):
    return templating.TemplateResponse(request, "profile.html")

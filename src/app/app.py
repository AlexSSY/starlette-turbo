from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

from . import settings, routes, middlewares, db
from .models import Base


async def lifespan_callback(app: Starlette):
    db.create_db(Base)
    yield


app = Starlette(
    debug=settings.DEBUG,
    lifespan=lifespan_callback,
    routes=routes.routes,
    middleware=middlewares.middlewares,
)

staticfiles_app = StaticFiles(directory=settings.STATICFILES_DIR)
app.mount("/static", staticfiles_app, "static")

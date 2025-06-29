import json
from starlette.requests import Request

from . import settings


def default(reqeust: Request):
    return {"page_title": "Main"}


def manifest(request: Request):
    with open(settings.JS_MANIFEST_FILE) as f:
        manifest = json.load(f)

    return {"js_file": manifest['src/main.js']['file']}

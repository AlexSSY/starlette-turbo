from starlette.requests import Request


def default(reqeust: Request):
    return {"page_title": "Main"}

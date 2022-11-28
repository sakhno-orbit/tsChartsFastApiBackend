from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


class CustomMW(BaseHTTPMiddleware):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)

    async def dispatch(self, request, call_next):
        print("{} {}".format(datetime.now(), (request.method, request.url)))
        response = await call_next(request)
        return response


DEFAULT_ORIGINS = (
    'http://localhost:8000',
    'http://127.0.0.1/8000',
    'http://localhost:4200',
    'http://127.0.0.1:4200',
)
origins = DEFAULT_ORIGINS

server_allow_methods = [
    # "DELETE",
    "GET",
    "HEAD",
    "OPTIONS",
    # "PATCH",
    # "POST",
    # "PUT"
]


class CustomCorsMiddleware(CORSMiddleware):

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=server_allow_methods,
            allow_headers=["*"],
        )

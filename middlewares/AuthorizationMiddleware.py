# from starlette.middleware.base import BaseHTTPMiddleware


def authorization_middleware(request, call_next):
    call_next(request)
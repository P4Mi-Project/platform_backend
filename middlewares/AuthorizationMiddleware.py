# from starlette.middleware.base import BaseHTTPMiddleware
from configs.firebase_admin_config import firebase_app
from configs.config import middleware_exclude_paths


async def authorization_middleware(request, call_next):
    if request.url.path in middleware_exclude_paths:
        await call_next(request)
    else:
        auth_header = request.headers.get("Authorization", None)
        if auth_header is not None:
            token = auth_header.split(" ")[1]
            # now need to verify the token against the firebase
            
    return request
# from starlette.middleware.base import BaseHTTPMiddleware
from configs.firebase_admin_config import firebase_app
from configs.config import middleware_exclude_paths
from configs.firebase_admin_config import verify_token
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.exceptions import HTTPException


class AuthMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self,request, call_next):
        try:
            print("Hello world the middleware is working.")
            
            # if request.url.path in middleware_exclude_paths:
            #     response = await call_next(request)
            #     return response
            # else:
                # auth_header = request.headers.get("Authorization", None)
                # if auth_header is not None:
                #     token = auth_header.split(" ")[1]
                #     if len(token) > 0:
                #         # now need to verify the token against the firebase
                #         info = verify_token(token)
                #         if len(info) == 0:
                #             pass
                #         else:
                #             await call_next(request)
                #             return request
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to fetch the auth header from the user request. Please have a look at the log.")
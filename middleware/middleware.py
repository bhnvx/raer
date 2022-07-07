import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response


class TimeHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        st_time = time.time()
        res = await call_next(request)
        ps_time = time.time() - st_time
        res.headers['X-Process-Time'] = str(ps_time)
        return res
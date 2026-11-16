import logging
import time
import uuid

from fastapi import FastAPI, Request

from app.api.v1.routes import router as app_router
from app.core.exceptions import register_exception_handler
from app.core.logging import request_id_ctx, setup_logging

setup_logging()

app = FastAPI(title="APP Name")
register_exception_handler(app)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex[:12]
    token = request_id_ctx.set(request_id)
    start = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        logger.exception("Unhandled error: %s %s", request.method, request.url.path)
        raise
    else:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "%s %s -> %d (%.1fms)",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )
        response.headers["X-Request-ID"] = request_id
        return response
    finally:
        request_id_ctx.reset(token)

app.include_router(
    app_router,
    prefix="/api/v1"
)
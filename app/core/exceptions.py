from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class AppError(Exception):
    """
    Errors That reach as a JSONResponse
    """
    status_code: int = status.HTTP_400_BAD_REQUEST
    def __init__(self, message:str):
        self.message = message
        super().__init__(message)

class NotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND

class ConflictError(AppError):
    status_code = status.HTTP_409_CONFLICT

class BadRequest(AppError):
    status_code = status.HTTP_400_BAD_REQUEST

class Unauthorized(AppError):
    status_code = status.HTTP_401_UNAUTHORIZED

class ForbiddenError(AppError):
    status_code = status.HTTP_403_FORBIDDEN

async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(content={"detail": exc.message}, status_code=exc.status_code)

def register_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(AppError, app_error_handler)
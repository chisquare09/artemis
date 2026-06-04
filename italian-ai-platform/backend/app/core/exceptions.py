from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(code="NOT_FOUND", message=message, status_code=404)


class ValidationException(AppException):
    def __init__(self, message: str = "Validation error"):
        super().__init__(code="VALIDATION_ERROR", message=message, status_code=422)


class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(code="BAD_REQUEST", message=message, status_code=400)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": {"code": exc.code, "message": exc.message}},
        )

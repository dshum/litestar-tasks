from litestar import Response, Request, MediaType
from litestar.exceptions import ValidationException, HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR


def validation_exception_handler(request: Request, exc: ValidationException) -> Response:
    return Response(
        media_type=MediaType.TEXT,
        content=f"Validation error: {exc.detail}",
        status_code=exc.status_code,
    )


def http_exception_handler(_: Request, exc: HTTPException) -> Response:
    return Response(
        media_type=MediaType.TEXT,
        content=f"HTTP error: {exc.detail}",
        status_code=exc.status_code,
    )


def internal_server_error_handler(request: Request, exc: Exception) -> Response:
    return Response(
        media_type=MediaType.TEXT,
        content=f"Server error: {exc}",
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )

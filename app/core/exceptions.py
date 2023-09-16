from litestar import Response, Request, MediaType
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR


def http_exception_handler(_: Request, exc: Exception) -> Response:
    """Default handler for exceptions subclassed from HTTPException."""
    status_code = getattr(exc, "status_code", HTTP_500_INTERNAL_SERVER_ERROR)
    detail = getattr(exc, "detail", "")

    return Response(
        media_type=MediaType.TEXT,
        content=detail,
        status_code=status_code,
    )

from litestar import Router

from api import drafts, board

__all__ = ["create_router"]


def create_router() -> Router:
    return Router(
        path="/",
        route_handlers=[drafts.DraftController, board.BoardController],
        signature_namespace={},
    )

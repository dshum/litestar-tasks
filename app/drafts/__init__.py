from litestar import Router

from .controllers import DraftController

draft_router = Router(path="/drafts", route_handlers=[DraftController])

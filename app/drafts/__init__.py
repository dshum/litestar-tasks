from litestar import Router

from app.drafts.controllers import DraftController

draft_router = Router(path="/drafts", route_handlers=[DraftController])

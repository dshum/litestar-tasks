from litestar import Router

from .controllers import UserController

user_router = Router(path="/users", route_handlers=[UserController])

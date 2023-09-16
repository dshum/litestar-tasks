from litestar import Router

from app.user.controllers import UserController

user_router = Router(path="/users", route_handlers=[UserController])

from litestar import Controller, get
from pydantic import UUID4


class UserController(Controller):
    @get(path="/{id:uuid}")
    async def get_user(self, id: UUID4) -> dict[str, UUID4]:
        return {"id": id}

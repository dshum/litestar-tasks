# ruff: noqa: B008
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Controller, delete, get, post, put
from litestar.di import Provide
from litestar.status_codes import HTTP_200_OK

from domain.tasks import ReadDTO, Repository, Service, WriteDTO

if TYPE_CHECKING:
    from litestar.repository import FilterTypes
    from sqlalchemy.ext.asyncio import AsyncSession

    from domain.tasks import Task

__all__ = [
    "TaskController",
]

DETAIL_ROUTE = "/{task_id:int}"


def provides_service(db_session: AsyncSession) -> Service:
    """Constructs repository and service objects for the request."""
    return Service(Repository(session=db_session, auto_commit=True))


class TaskController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    path = "/tasks"
    dependencies = {"service": Provide(provides_service, sync_to_thread=False)}
    tags = ["Tasks"]

    @get()
    async def get_tasks(self, service: Service) -> list[Task]:
        """Get a list of tasks."""
        return await service.list()

    @post()
    async def create_task(self, data: Task, service: Service) -> Task:
        """Create a Task."""
        return await service.create(data)

    @get(DETAIL_ROUTE)
    async def get_task(self, service: Service, task_id: int) -> Task:
        """Get Task by ID."""
        return await service.get(task_id)

    @put(DETAIL_ROUTE)
    async def update_task(self, data: Task, service: Service, task_id: int) -> Task:
        """Update Task."""
        return await service.update(task_id, data)

    @delete(DETAIL_ROUTE, status_code=HTTP_200_OK)
    async def delete_task(self, service: Service, task_id: int) -> Task:
        """Delete Task by ID."""
        return await service.delete(task_id)

# ruff: noqa: B008
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import Controller, delete, get, post, put
from litestar.di import Provide
from litestar.status_codes import HTTP_200_OK

from domain.projects import ReadDTO, Repository, Service, WriteDTO

if TYPE_CHECKING:
    from litestar.repository import FilterTypes
    from sqlalchemy.ext.asyncio import AsyncSession

    from domain.projects import Project

__all__ = [
    "ProjectController",
]

DETAIL_ROUTE = "/{project_id:int}"


def provides_service(db_session: AsyncSession) -> Service:
    """Constructs repository and service objects for the request."""
    return Service(Repository(session=db_session, auto_commit=True))


class ProjectController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    path = "/projects"
    dependencies = {"service": Provide(provides_service, sync_to_thread=False)}
    tags = ["Projects"]

    @get()
    async def get_projects(self, service: Service) -> list[Project]:
        """Get a list of projects."""
        return await service.list()

    @post()
    async def create_project(self, data: Project, service: Service) -> Project:
        """Create a Project."""
        return await service.create(data)

    @get(DETAIL_ROUTE)
    async def get_project(self, service: Service, project_id: int) -> Project:
        """Get Project by ID."""
        return await service.get(project_id)

    @put(DETAIL_ROUTE)
    async def update_project(self, data: Project, service: Service, project_id: int) -> Project:
        """Update Project."""
        return await service.update(project_id, data)

    @delete(DETAIL_ROUTE, status_code=HTTP_200_OK)
    async def delete_project(self, service: Service, project_id: int) -> Project:
        """Delete Project by ID."""
        return await service.delete(project_id)

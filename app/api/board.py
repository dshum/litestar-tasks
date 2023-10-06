from typing import Any

from litestar import Controller, get
from litestar.response import Template
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.board.models import Project


class BoardController(Controller):
    path = "/"

    @get(path="/projects", name="projects")
    async def get_projects(self, db_session: AsyncSession) -> Template:
        projects = [project for project in list(await db_session.scalars(select(Project)))]
        return Template(template_name="projects.html", context={"projects": projects})

    @get(path="/projects/{project_id:int}", name="project")
    async def get_project(self, project_id: int, db_session: AsyncSession) -> Template:
        project = await db_session.get(Project, project_id)
        tasks = project.tasks
        return Template(template_name="project.html", context={"project": project, "tasks": tasks})

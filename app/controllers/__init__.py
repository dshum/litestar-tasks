from litestar import Router

from domain.projects import Project
from domain.tasks import Task

from . import board, drafts, projects, tasks

__all__ = ["create_router", "create_html_router"]


def create_router() -> Router:
    return Router(
        path="/api",
        route_handlers=[projects.ProjectController, tasks.TaskController],
        signature_namespace={"Project": Project, "Task": Task},
    )


def create_html_router() -> Router:
    return Router(
        path="/",
        route_handlers=[board.BoardController, drafts.DraftController],
        signature_namespace={}
    )

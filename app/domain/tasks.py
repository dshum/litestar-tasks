from abc import ABC
from typing import Annotated

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.dto import DTOConfig
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from domain.projects import Project
from lib import service

__all__ = [
    "Task",
    "ReadDTO",
    "Repository",
    "Service",
    "WriteDTO",
]


class Task(BigIntAuditBase):
    title: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project: Mapped[Project] = relationship(lazy="joined", innerjoin=True, viewonly=True)


class Repository(SQLAlchemyAsyncRepository[Task], ABC):
    model_type = Task
    auto_commit = True


class Service(service.Service[Task]):
    repository_type = Repository


write_config = DTOConfig(exclude={"id", "project", "created_at", "updated_at"})
WriteDTO = SQLAlchemyDTO[Annotated[Task, write_config]]
ReadDTO = SQLAlchemyDTO[Task]

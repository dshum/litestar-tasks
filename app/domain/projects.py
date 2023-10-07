from abc import ABC
from typing import Annotated, TYPE_CHECKING

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO
from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from litestar.dto import DTOConfig
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, relationship, mapped_column

from lib import service

if TYPE_CHECKING:
    from domain.tasks import Task

__all__ = [
    "Project",
    "ReadDTO",
    "Repository",
    "Service",
    "WriteDTO",
]


class Project(BigIntAuditBase):
    title: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    tasks: Mapped[list["Task"]] = relationship(back_populates="project", lazy="selectin")


class Repository(SQLAlchemyAsyncRepository[Project], ABC):
    model_type = Project


class Service(service.Service[Project]):
    repository_type = Repository


write_config = DTOConfig(exclude={"id", "tasks", "created_at", "updated_at"})
WriteDTO = SQLAlchemyDTO[Annotated[Project, write_config]]
ReadDTO = SQLAlchemyDTO[Project]

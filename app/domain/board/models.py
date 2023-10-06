from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

__all__ = ["Project", "Task"]


class Project(BigIntAuditBase):
    title: Mapped[str]
    description: Mapped[Text] = mapped_column(Text)
    tasks: Mapped[list["Task"]] = relationship(back_populates="project", lazy="selectin")


class Task(BigIntAuditBase):
    title: Mapped[str]
    content: Mapped[Text] = mapped_column(Text)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project: Mapped[Project] = relationship(lazy="joined", innerjoin=True, viewonly=True)

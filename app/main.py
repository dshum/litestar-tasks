from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException
from litestar.response import Template
from litestar.static_files import StaticFilesConfig
from litestar.template import TemplateConfig

from app.core.exceptions import http_exception_handler
from app.drafts import draft_router
from app.user import user_router


@get("/", name="index")
async def index() -> Template:
    return Template(template_name="hello.html")


app = Litestar(
    route_handlers=[index, draft_router, user_router],
    template_config=TemplateConfig(
        directory=[Path("app/templates"), Path("app/drafts/templates")],
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(directories=["app/static"], path="/", name="static"),
    ],
    exception_handlers={HTTPException: http_exception_handler},
)

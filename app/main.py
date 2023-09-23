from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException, ValidationException
from litestar.response import Template
from litestar.static_files import StaticFilesConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.template import TemplateConfig

from api.router import create_router
from lib import sentry
from lib.db import sqlalchemy_plugin
from lib.exceptions import (
    http_exception_handler,
    internal_server_error_handler,
    validation_exception_handler
)


@get("/", name="index")
async def index() -> Template:
    return Template(template_name="hello.html")


app = Litestar(
    route_handlers=[index, create_router()],
    dependencies={},
    on_startup=[sentry.configure, sqlalchemy_plugin.on_startup],
    plugins=[sqlalchemy_plugin.plugin],
    exception_handlers={
        ValidationException: validation_exception_handler,
        HTTPException: http_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: internal_server_error_handler,
    },
    template_config=TemplateConfig(
        directory=[Path("templates"), Path("domain/drafts/templates")],
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/", name="static"),
    ]
)

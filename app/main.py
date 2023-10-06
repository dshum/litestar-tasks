from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.exceptions import HTTPException, ValidationException, NotFoundException
from litestar.response import Template
from litestar.static_files import StaticFilesConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.template import TemplateConfig

from api.router import create_router
from lib import sentry, settings
from lib.commands.test import TestCLIPlugin
from lib.db import sqlalchemy_plugin
from lib.exceptions import (
    http_exception_handler,
    internal_server_error_handler,
    validation_exception_handler,
    not_found_exception_handler
)


@get("/", name="index")
async def index() -> Template:
    return Template(template_name="hello.html")


@get("/favicon.ico", name="favicon")
async def favicon() -> str:
    return "favicon"


app = Litestar(
    debug=settings.app.DEBUG,
    route_handlers=[index, favicon, create_router()],
    dependencies={},
    on_startup=[sentry.configure],
    plugins=[sqlalchemy_plugin.plugin, TestCLIPlugin()],
    exception_handlers={
        # ValidationException: validation_exception_handler,
        NotFoundException: not_found_exception_handler,
        # HTTPException: http_exception_handler,
        # HTTP_500_INTERNAL_SERVER_ERROR: internal_server_error_handler,
    },
    template_config=TemplateConfig(
        directory=[Path("templates"), Path("domain/drafts/templates"), Path("domain/board/templates")],
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/", name="static"),
    ]
)

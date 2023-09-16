from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.di import Provide
from litestar.exceptions import HTTPException, LitestarException, ValidationException
from litestar.response import Template
from litestar.static_files import StaticFilesConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.template import TemplateConfig

from core.exceptions import http_exception_handler, internal_server_error_handler, validation_exception_handler
from core.settings import Settings
from drafts import draft_router
from users import user_router


@get("/", name="index")
async def index() -> Template:
    return Template(template_name="hello.html")


async def get_settings() -> Settings:
    return Settings()


app = Litestar(
    route_handlers=[index, draft_router, user_router],
    dependencies={
        "settings": Provide(get_settings, use_cache=True),
    },
    template_config=TemplateConfig(
        directory=[Path("templates"), Path("drafts/templates")],
        engine=JinjaTemplateEngine,
    ),
    static_files_config=[
        StaticFilesConfig(directories=["static"], path="/", name="static"),
    ],
    exception_handlers={
        ValidationException: validation_exception_handler,
        HTTPException: http_exception_handler,
        HTTP_500_INTERNAL_SERVER_ERROR: internal_server_error_handler,
    },
)

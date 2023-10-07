import json
import os

from litestar import Controller, get
from litestar.exceptions import LitestarException
from litestar.response import Template

from lib.settings import BASE_DIR


class DraftController(Controller):
    path = "/drafts"

    @get(path="/board", name="board")
    async def get_board(self) -> Template:
        return Template(template_name="drafts/board.html")

    @get(path="/db", name="db")
    async def get_db_schema(self) -> Template:
        path = os.path.join(BASE_DIR, "domain", "drafts", "resources", "db.json")
        with open(path) as f:
            tables = json.load(f)
        return Template(template_name="drafts/db.html", context={"tables": tables})

    @get(path="/links", name="links")
    async def get_links(self) -> Template:
        return Template(template_name="drafts/links.html")

    @get(path="/error/{name:str}", name="error")
    async def get_error(self, name: str) -> Template:
        raise LitestarException(name)

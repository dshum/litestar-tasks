import json
import os
from pathlib import Path

from litestar import Controller, get
from litestar.response import Template
from pydantic import UUID4

from lib.settings import BASE_DIR


class DraftController(Controller):
    path = "/drafts"

    @get(path="/board", name="board")
    async def get_board(self) -> Template:
        return Template(template_name="board.html")

    @get(path="/db", name="db")
    async def get_db_schema(self) -> Template:
        path = os.path.join(BASE_DIR, "domain", "drafts", "resources", "db.json")
        with open(path) as f:
            tables = json.load(f)
        return Template(template_name="db.html", context={"tables": tables})

    @get(path="/links", name="links")
    async def get_links(self) -> Template:
        return Template(template_name="links.html")

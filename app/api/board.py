from litestar import Controller, get
from litestar.response import Template


class BoardController(Controller):
    path = "/api"

    @get(path="/projects", name="projects")
    async def get_projects(self) -> Template:
        return Template(template_name="board.html")

from litestar import Litestar
from litestar_granian import GranianPlugin

from src.controllers import UserController
from src.database import sqlalchemy_plugin

app = Litestar(
    route_handlers=[UserController],
    plugins=[GranianPlugin(), sqlalchemy_plugin],
    # on_startup=[on_startup]
)
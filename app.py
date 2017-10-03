import settings
from db.vas3kru import Vas3kDatabase
from godmode import GodModeApp
from models.index import IndexAdminModel
from models.vas3k_365 import The365AdminModel
from models.vas3k_clickers import ClickersAdminModel
from models.vas3k_comments import CommentAdminModel
from models.vas3k_memories import MemoryAdminModel
from models.vas3k_stories import StoryAdminModel

app = GodModeApp(
    databases=[Vas3kDatabase],
    models=[
        IndexAdminModel,
        StoryAdminModel,
        MemoryAdminModel,
        CommentAdminModel,
        ClickersAdminModel,
        The365AdminModel,
    ]
)

if settings.DEBUG:
    app.run()

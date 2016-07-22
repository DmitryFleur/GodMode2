from base.model import BaseAdminModel
from base.view import BaseView
from common.acl import ACL
from db.demo import DemoDatabase


class IndexAdminModel(BaseAdminModel):
    acl = ACL.ALL
    db = DemoDatabase
    title = "Home"
    place = None
    url_prefix = "/"

    class DemoIndexView(BaseView):
        acl = ACL.ALL
        url = "/"
        title = "Index"
        template = "index.html"

        def get(self):
            return self.render()

    list_view = DemoIndexView

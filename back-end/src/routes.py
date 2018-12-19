import json

from src.handler import blog, user

import logging
from logging import getLogger

logger = getLogger("my-blog").getChild("sub")


def set_routes(api):
    @api.route("/users")
    class UserListResource:
        def on_get(self, req, resp):
            resp.media = user.get_user_list()

        async def on_post(self, req, resp):
            try:
                req_data = await req.media()
                resp.status_code = api.status_codes.HTTP_201
                resp.media = json.dumps(user.add_user(req_data))
            except Exception as e:
                resp.status_code = api.status_codes.HTTP_500
                resp.media = json.dumps({ "error": "fuck" })
                logger.error(e)

    @api.route("/users/{id}")
    class UserResource:
        def on_get(self, req, resp, *, id):
            resp.media = user.get_user_by_id(id)

        def on_delete(self, req, resp, *, id):
            user.delete_user(id)

    @api.route("/blog")
    class BlogListResource:
        def on_get(self, req, resp):
            resp.media = blog.get_blog_list()

        def on_post(self, req, resp):
            pass

    @api.route("/blog/{id}")
    class BlogResource:
        def on_get(self, req, resp, *, id):
            resp.media = blog.get_blog_by_id(id)

        def on_delete(self, req, resp, *, id):
            blog.delete_blog(id)
            pass

    return api

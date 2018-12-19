import json

from src.handler import blog, user

import logging
from logging import getLogger
from responder import API
from responder.models import Request, Response
from sqlalchemy.exc import IntegrityError

logger = getLogger("my-blog").getChild(__name__)


def set_routes(api: API):
    @api.route("/users")
    class UserListResource:
        def on_get(self, req: Request, resp: Response):
            resp.media = user.get_user_list()

        async def on_post(self, req: Request, resp: Response):
            try:
                req_data = await req.media()
                resp.status_code = api.status_codes.HTTP_201
                resp.media = user.add_user(req_data)
            except Exception as e:
                # https://tools.ietf.org/html/rfc7807
                resp.headers["Content-Type"]     = "application/problem+json"
                resp.headers["Content-Language"] = "en"
                logger.error(e)
                if isinstance(e, IntegrityError):
                    logger.error(e)
                    logger.error(e.args)
                    resp.status_code = api.status_codes.HTTP_400
                    resp.text = json.dumps({
                        "type": "about:blank",
                        "title": e.args,
                        "detail": "Your current balance is 30, but that costs 50.",
                        "instance": "/account/12345/msgs/abc",
                    })

    @api.route("/users/{id}")
    class UserResource:
        def on_get(self, req: Request, resp: Response, *, id):
            resp.media = user.get_user_by_id(id)

        def on_delete(self, req: Request, resp: Response, *, id):
            user.delete_user(id)

    @api.route("/blog")
    class BlogListResource:
        def on_get(self, req: Request, resp: Response):
            resp.media = blog.get_blog_list()

        def on_post(self, req: Request, resp: Response):
            pass

    @api.route("/blog/{id}")
    class BlogResource:
        def on_get(self, req: Request, resp: Response, *, id):
            resp.media = blog.get_blog_by_id(id)

        def on_delete(self, req: Request, resp: Response, *, id):
            blog.delete_blog(id)
            pass

    return api

import json

from src.handler import blog, user


def set_routes(api):
    @api.route("/users")
    class UserListResource:
        def on_get(self, req, resp):
            resp.media = user.get_user_list()

        async def on_post(self, req, resp):
            req_data = await req.media()
            resp.media = user.add_user(req_data)

    @api.route("/users/{id}")
    class UserResource:
        def on_get(self, req, resp, *, id):
            resp.media = user.get_user_by_id(id)

        def on_delete(self, req, resp, *, id):
            user.delete_user(id)
            pass

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

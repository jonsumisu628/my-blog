import json

from src.handler import blog, user


def set_routes(api):
    @api.route("/users")
    class UserListResource:
        def on_get(self, req, resp, *, id):
            resp.media = user.get_user_list()

        def on_post(self, req, resp, *, id):
            pass

    @api.route("/users/{id}")
    class UserResource:
        def on_get(self, req, resp, *, id):
            resp.media = user.get_user_by_id(id)

        def on_post(self, req, resp, *, id):
            pass

    @api.route("/blog")
    class BlogListResource:
        def on_get(self, req, resp, *, id):
            resp.media = blog.get_blog_list()

        def on_post(self, req, resp, *, id):
            pass

    @api.route("/blog/{id}")
    class BlogResource:
        def on_get(self, req, resp, *, id):
            resp.media = blog.get_blog_by_id(id)

        def on_post(self, req, resp, *, id):
            pass

    return api

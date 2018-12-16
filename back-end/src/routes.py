import json

from src.handler import blog, user


class UserListEndpoint:
    def on_get(self, req, resp, *, id):
        resp.media = user.get_user_list()

    def on_post(self, req, resp, *, id):
        pass

class UserEndpoint:
    def on_get(self, req, resp, *, id):
        resp.media = user.get_user_by_id(id)

    def on_post(self, req, resp, *, id):
        pass

class BlogListEndpoint:
    def on_get(self, req, resp, *, id):
        resp.media = blog.get_blog_list()

    def on_post(self, req, resp, *, id):
        pass

class BlogEndpoint:
    def on_get(self, req, resp, *, id):
        resp.media = blog.get_blog_by_id(id)

    def on_post(self, req, resp, *, id):
        pass

def set_routes(api):
    api.add_route("/users", UserListEndpoint)
    api.add_route("/users/{id}", UserListEndpoint)
    api.add_route("/blog", BlogListEndpoint)
    api.add_route("/blog/{id}", BlogEndpoint)

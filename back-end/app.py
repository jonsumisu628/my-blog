import os

import responder
from dotenv import load_dotenv

from src.routes import set_routes

cors_params = {
	"allow_origins": ("*"),
	"allow_methods": ("GET", "PUT", "POST", "DELETE"),
	"allow_headers": (),
	"allow_credentials": False,
	"allow_origin_regex": None,
	"expose_headers": (),
	"max_age": 600,
}

dotenv_path = "".join([os.path.dirname(__file__), '/.env'])
load_dotenv(dotenv_path)
mode = os.environ.get("MY_BLOG_MODE")

if __name__ == '__main__':
    api = responder.API(
        debug=True,
        cors=True,
        cors_params=cors_params,
    )
    set_routes(api)
    api.run(
        address='0.0.0.0',
        port=80,
        debug=True if mode == "dev" else False
    )

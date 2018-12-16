from src.routes import set_routes

import responder

cors_params = {
	"allow_origins": ("*"),
	"allow_methods": ("GET", "PUT", "POST", "DELETE"),
	"allow_headers": (),
	"allow_credentials": False,
	"allow_origin_regex": None,
	"expose_headers": (),
	"max_age": 600,
}

if __name__ == '__main__':
    # TODO: set CORS
    api = responder.API(
        debug=True,
        cors=True,
        cors_params=cors_params,
    )
    set_routes(api)
    api.run(address='0.0.0.0', port=80, debug=True)

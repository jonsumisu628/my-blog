import logging
import os
from logging import Formatter, StreamHandler, getLogger

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
    logger = getLogger("my-blog")
    logger.setLevel(
        logging.DEBUG if mode == "dev" else logging.INFO
    )

    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)

    logger.info("""
 .----------------.  .----------------.
| .--------------. || .--------------. |
| | ____    ____ | || |  ____  ____  | |
| ||_   \  /   _|| || | |_  _||_  _| | |
| |  |   \/   |  | || |   \ \  / /   | |
| |  | |\  /| |  | || |    \ \/ /    | |
| | _| |_\/_| |_ | || |    _|  |_    | |
| ||_____||_____|| || |   |______|   | |
| |              | || |              | |
| '--------------' || '--------------' |
 '----------------'  '----------------'
 .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |   _____      | || |     ____     | || |    ______    | |
| |  |_   _ \    | || |  |_   _|     | || |   .'    `.   | || |  .' ___  |   | |
| |    | |_) |   | || |    | |       | || |  /  .--.  \  | || | / .'   \_|   | |
| |    |  __'.   | || |    | |   _   | || |  | |    | |  | || | | |    ____  | |
| |   _| |__) |  | || |   _| |__/ |  | || |  \  `--'  /  | || | \ `.___]  _| | |
| |  |_______/   | || |  |________|  | || |   `.____.'   | || |  `._____.'   | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'
 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |      __      | || |   ______     | || |     _____    | |
| |     /  \     | || |  |_   __ \   | || |    |_   _|   | |
| |    / /\ \    | || |    | |__) |  | || |      | |     | |
| |   / ____ \   | || |    |  ___/   | || |      | |     | |
| | _/ /    \ \_ | || |   _| |_      | || |     _| |_    | |
| ||____|  |____|| || |  |_____|     | || |    |_____|   | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'
    """)

    api = responder.API(
        debug=True,
        cors=True,
        cors_params=cors_params,
    )
    set_routes(api)

    logger.info("""
=======================================
Booting...
address: %s
port   : %s
mode   : %s
=======================================
    """ % ("0.0.0.0", 80, mode))
    api.run(
        address='0.0.0.0',
        port=80,
        debug=True if mode == "dev" else False
    )

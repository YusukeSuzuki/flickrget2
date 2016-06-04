import sys

from flickrapi import FlickrAPI
from .config import get_config, set_token, CONFIG_APP_KEY, CONFIG_APP_SECRET
from .args import get_arg_parser

def run():
    app_config = get_config()
    api = FlickrAPI(
        app_config[CONFIG_APP_KEY], app_config[CONFIG_APP_SECRET],
        format='json')
    app_config, api = set_token(app_config, api)

    parser = get_arg_parser()
    namespace = parser.parse_args()

    if namespace.target is not None and namespace.target:
        namespace.func(api, namespace)
    else:
        parser.print_help()


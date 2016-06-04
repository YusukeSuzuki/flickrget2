import os, sys
import webbrowser
from pathlib import Path

import appdirs
import yaml

APP_NAME = 'flickrget'
SETTING_FILE_NAME = 'config.yaml'

CONFIG_APP_KEY = 'app_key'
CONFIG_APP_SECRET = 'secret_key'

CONFIG_USER_TOKEN = 'user_token'

def get_config_file_path():
    path = Path(appdirs.user_config_dir(), APP_NAME, SETTING_FILE_NAME)
    return path

def get_config_from_file(path):
    if not path.exists():
        return {}

    with path.open() as f:
        return yaml.load(f) or {}

def dump_config_to_file(path, app_config):
    if not path.exists():
        path.parent.mkdir(parents=True)
    
    with path.open(mode='w') as  f:
        f.write(yaml.dump(app_config))

def ask_keys(app_config):
    sys.stdout.write('enter flickr app key: ')
    app_config[CONFIG_APP_KEY] = str(input())
    sys.stdout.write('enter flickr app secret: ')
    app_config[CONFIG_APP_SECRET] = str(input())
    return app_config

def get_config():
    path = get_config_file_path()
    app_config = get_config_from_file(path)

    if CONFIG_APP_SECRET not in app_config or CONFIG_APP_KEY not in app_config:
        app_config = ask_keys(app_config)
        dump_config_to_file(path, app_config)

    if CONFIG_APP_SECRET not in app_config or CONFIG_APP_KEY not in app_config:
        print('no app key and secret')
        exit()

    return app_config

def set_token(app_config, api):
    if api.token_valid(perms='read'):
        return app_config, api

    print('token lost')
    api.get_request_token(oauth_callback='oob')
    auth_url = api.auth_url(perms='read')
    webbrowser.open_new_tab(auth_url)

    sys.stdout.write('input token: ')
    token = str(input())
    api.get_access_token(token)

    if not api.token_valid(perms='read'):
        print('token error')
        exit()

    return app_config, api


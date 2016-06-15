import argparse
from .sub_commands import *

COMMON_OPTIONS = [
    ('--max', int, -1),
]

def get_arg_parser():
    parser = argparse.ArgumentParser(description='flickr search utility')
    parser.set_defaults(target='')
    sub_parsers = parser.add_subparsers(title='sub commands')

    # tags
    sub_parser = sub_parsers.add_parser('tags')
    sub_parser.set_defaults(target='tags')
    sub_parser.set_defaults(func=tag_search)

    sub_parser.add_argument('tags', metavar='Tag', type=str, nargs='+', help='tags for search')

    for opt in COMMON_OPTIONS:
        sub_parser.add_argument(opt[0], type=opt[1], default=opt[2])
    
    sub_parser.add_argument('--orientation', type=str, choices=[ONLY_PORTRAIT, ONLY_LANDSCAPE], default=None)
    sub_parser.add_argument('--json', action='store_true')

    # words

    # random

    return parser


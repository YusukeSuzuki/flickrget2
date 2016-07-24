import json
import sys

ONLY_PORTRAIT = 'portrait'
ONLY_LANDSCAPE = 'landscape'

URL_TYPES = ['sq', 't', 's', 'q', 'm', 'n', 'z', 'c', 'l', 'o']

def tag_search(api, args):
    page, pages = (0, 1)
    out_num = 0
    out_max = 0 if args.max < 0 else args.max

    portrait_only = args.orientation == ONLY_PORTRAIT
    landscape_only = args.orientation == ONLY_LANDSCAPE

    url_type = args.size
    url_tag = 'url_' + url_type
    width_tag = 'width_' + url_type
    height_tag = 'height_' + url_type

    while page < pages and min(out_max, out_num) != args.max:
        json_res = api.photos.search(
            tags=','.join(args.tags), page=page,
            extras=','.join([url_tag,'original_format']),
            tag_mode='all')

        if not json_res:
            break

        res_dict = json.loads(json_res.decode())['photos']

        pages = int(res_dict['pages'])
        page = int(res_dict['page'])

        for photo in res_dict['photo']:
            if url_tag not in photo:
                continue

            width = int(photo[width_tag])
            height = int(photo[height_tag])

            if portrait_only and (width > height):
                continue
            if landscape_only and (width < height):
                continue

            if args.json:
                print(photo)
            else:
                print(photo[url_tag])
            
            out_num = out_num + 1

            if min(out_max, out_num) == args.max:
                break

        page = page + 1


import json
import sys

def tag_search(api, args):
    page, pages = (0, 1)
    out_num = 0
    out_max = 0 if args.max < 0 else args.max

    #print(args.tags, file=sys.stderr)

    while page < pages and min(out_max, out_num) != args.max:
        json_res = api.photos.search(
            tags=','.join(args.tags), page=(page+1), extras=['url_l'],
            tag_mode='all')

        if not json_res:
            break

        res_dict = json.loads(json_res.decode())['photos']

        pages = int(res_dict['pages'])
        page = int(res_dict['page'])

        for photo in res_dict['photo']:
            if 'url_l' in photo:
                print(photo['url_l'])
                out_num = out_num + 1

            if min(out_max, out_num) == args.max:
                break


import json
from sys import float_repr_style
import requests


def getVideoLink(topicId):
    headers = {
        'authority': 'api.penpencil.xyz',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer 5909325ce3820585405f3c46c5bc13a17089394770335c464b58c065b8dbc01c',
        'cache-control': 'no-cache',
        'client-id': '5eb393ee95fab7468a79d189',
        'client-type': 'WEB',
        'client-version': '99',
        'origin': 'https://study.physicswallah.live',
        'pragma': 'no-cache',
        'randomid': '22ad4076-7a15-4454-b616-61fdedb997bd',
                    'referer': 'https://study.physicswallah.live/',
                    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    }

    params = {
        'page': '1',
        'contentType': 'videos',
        # 'tag': '61612c214044e0001819ff92',
        'tag': topicId,
    }

    response = requests.get(
        'https://api.penpencil.xyz/v2/batches/613f3f0b09fa3d001891a954/subject/613f3f7057bc670018c7f645/contents', params=params, headers=headers)
    jsonData = json.loads(response.text)

    return jsonData['data']


# getVideoLink('6141a9e4157e24001234eef8')

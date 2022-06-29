import requests
import json


def get_policy(baseUrl):

    headers = {
        'authority': 'api.penpencil.xyz',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer 5909325ce3820585405f3c46c5bc13a17089394770335c464b58c065b8dbc01c',
        'client-id': '5eb393ee95fab7468a79d189',
        'client-type': 'WEB',
        'client-version': '99',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://study.physicswallah.live',
        'randomid': 'c17ff79f-2365-443c-8940-314539d86822',
        'referer': 'https://study.physicswallah.live/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    }

    json_data = {
        # 'url': 'https://d1d34p8vz63oiq.cloudfront.net/d9a881a0-a627-43fa-960f-c8688f7aef67/master.mpd',
        'url': baseUrl,
    }

    response = requests.post(
        'https://api.penpencil.xyz/v1/files/get-signed-cookie', headers=headers, json=json_data)
    jsonData = json.loads(response.text)
    return jsonData['data']


# get_policy(
#     'https://d1d34p8vz63oiq.cloudfront.net/d9a881a0-a627-43fa-960f-c8688f7aef67/master.mpd')

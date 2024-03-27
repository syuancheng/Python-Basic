from urllib import request, parse
import json

# regions = ['SG', 'ID', 'TW', 'BR', 'TH', 'PH', 'MY', 'VN', 'MX', 'CL', 'CO']
regions = ['SG']


bundleDict = {
    'daily_discover_main': 'http://mixer-dd-main.recommend.live-test.shopee.io/recommend',
    'product_detail_page': 'http://mixer-pdp-main.recommend.live-test.shopee.io/recommend?'
}

bundleConfig = {
    'daily_discover_main': 500,
    'product_detail_page': 200
}

for bundle, url in bundleDict.items():
    for country in regions:
        req = request.Request(url, method="POST")
        req.add_header('Content-Type', 'application/json')

        mixerReq = {
            "bundle": bundle,
            "country": country,
            "userid": 0,
            "offset": 0,
            "count": bundleConfig[bundle],
            "requestid": "emergency_static_file"
        }
        data = json.dumps(mixerReq)
        data = data.encode()

        r = request.urlopen(req, data=data)

        result = r.read()

        print(result)
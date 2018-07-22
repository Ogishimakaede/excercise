from django.shortcuts import render

import requests   # Web からデータを取ってくる時に使う

import json # 取得したjsonファイルをでコードするのに使う

import re



# APIキーの指定
apikey = "27a3ffdcc1d3729e3f3ca4dd852e71d5"

# 天気を調べたい都市の一覧
#cities = ["Tokyo,JP", "Osaka,JP", "Okinawa,JP"]

# APIのひな型
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏)
k2c = lambda k: k - 273.15

def appmain(request):

    cityname = request.GET.get(key='cityname',default="Tokyo")

    # APIのURLを得る
    url = api.format(city=cityname, key=apikey)

    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)

    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)

    # demo/main.hml に値を渡す
    return render(request, 'demo/main.html', {
        'city' : data["name"],
        'weather' : data["weather"][0]["description"],
        'max_temp' : round(k2c(data["main"]["temp_max"]),1),
        'min_temp' : round(k2c(data["main"]["temp_min"]),1),
        'humidity' : data["main"]["humidity"],
        'background' : "<img src=\"/static/exercise/" + re.sub(" ","",data["weather"][0]["description"]) + ".jpg\" class = \"image\">"
    })

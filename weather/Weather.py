import ui
import requests
import speech
import time
import datetime
from PIL import Image
import json
from geopy.geocoders import Nominatim
import time
from pprint import pprint
import raw
import decimal

geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
geo_data = requests.get(geo_request_url).json()
print(geo_data['latitude'])
print(geo_data['longitude'])
lat1 = geo_data['latitude']
lon1 = geo_data['longitude']
dt_now = datetime.datetime.now()
print(dt_now)
a = 11
hour = dt_now.hour
minute = dt_now.minute
if (hour > 19) or (hour <= 5):
	speech.say("こんばんわ。", "ja-JP", 0.5)
elif (hour > 11):
	speech.say("こんにちは。", "ja-JP", 0.5)
elif (hour > 5):
	speech.say("おはようございます。", "ja-JP", 0.5)
str1 = "今のお天気をお知らせします。ただいまの時刻は{}時{}分です。".format(hour, minute)
speech.say(str1, "ja-JP", 0.5)
"""YOUR_APIKEY"にはOPENWEATHERにて生成したKEYを入力してください。"""
API_KEY = "YOUR_APIKEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

#ここのシティの部分を変更すると別の地方でも使えます。
url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={key}"
url1 = url.format(lat=lat1, lon=lon1, key=API_KEY)
response = requests.get(url1)

data = response.json()
jsontext = json.dumps(data, indent=4)

print(jsontext)
f = open('Now.json', 'w', encoding='UTF-8')

f.write(jsontext)

f.close()
f1 = open('Now.json', 'r', encoding='UTF-8')
jsn = json.load(f1)
w = jsn["main"]
city = jsn["name"]
str3 = "{}は".format(city)
speech.say(str3, "ja-JP", 0.5)
rtn = "01n" in jsontext
if (rtn == True):
	speech.say("快晴です。夜空がよく見えるでしょう", "ja-JP", 0.5)
	a = 1
rtn = "02n" in jsontext
if (rtn == True):

	speech.say("少し雲がかかっています。", "ja-JP", 0.5)
	a = 2
rtn = "03n" in jsontext
if (rtn == True):
	speech.say("曇りです。", "ja-JP", 0.5)
	a = 3
rtn = "04n" in jsontext
if (rtn == True):
	speech.say("雲がかかっています。", "ja-JP", 0.5)
	a = 5
rtn = "09n" in jsontext
if (rtn == True):
	speech.say("雨雲がかかっていて少し雨が降っています。", "ja-JP", 0.5)
	a = 6
rtn = "010n" in jsontext
if (rtn == True):
	speech.say("雨が降っています。", "ja-JP", 0.5)
	a = 7
rtn = "011n" in jsontext
if (rtn == True):
	speech.say("らいうです。ところにより雷が落ちるので気をつけてください。", "ja-JP", 0.5)
	a = 8
rtn = "30n" in jsontext
if (rtn == True):
	speech.say("雪が降っています。", "ja-JP", 0.5)
	a = 9
rtn = "50n" in jsontext
if (rtn == True):
	speech.say("霧がかかっています。", "ja-JP", 0.5)
	a = 10
rtn = "01d" in jsontext
if (rtn == True):
	speech.say("快晴です。", "ja-JP", 0.5)
	a = 11
rtn = "02d" in jsontext
if (rtn == True):
	speech.say("少し雲がかかっています。", "ja-JP", 0.5)
	a = 12
rtn = "03d" in jsontext
if (rtn == True):
	speech.say("曇りです。", "ja-JP", 0.5)
	a = 13
rtn = "04d" in jsontext
if (rtn == True):
	speech.say("雲がかかっています。", "ja-JP", 0.5)
	a = 14
rtn = "09d" in jsontext
if (rtn == True):
	speech.say("雨雲がかかっていて少し雨が降っています。", "ja-JP", 0.5)
	a = 15
rtn = "010d" in jsontext
if (rtn == True):
	speech.say("雨が降っています。", "ja-JP", 0.5)
	a = 16
rtn = "011d" in jsontext
if (rtn == True):
	speech.say("らいうです。ところにより雷が落ちるので気をつけてください。", "ja-JP", 0.5)
	a = 17
rtn = "30d" in jsontext
if (rtn == True):
	speech.say("雪が降っています。", "ja-JP", 0.5)
	a = 18
rtn = "50d" in jsontext
if (rtn == True):
	speech.say("霧がかかっています。", "ja-JP", 0.5)
	a = 19

t = w['temp']
p = w["pressure"]
h = w["humidity"]
t = 1.8 * t + 32 - 273.15 * 1.8
t = ((t - 32)) / 1.8
t = round(t, 2)
print("気温は{}度です。".format(t))
str2 = "現在の気温はせっし{}度で、気圧は{}ヘクトパスカルです。湿度は{}パーセントでしょう。".format(t, p, h)
speech.say(str2, "ja-JP", 0.5)


#ボタンをタップした時の動作
def button_tapped(sender):
	sender.title = 'Stopped'
	speech.stop()
	v.close()


v = ui.load_view('botan.pyui')

if (a == 11):
	v['imageview1'].image = ui.Image('sunny.PNG')
if (a == 3) or (a == 13):
	v['imageview1'].image = ui.Image('cloudy.PNG')
if (a == 15) or (a == 6):
	v['imageview1'].image = ui.Image('rainy.PNG')
if (a == 8) or (a == 17):
	v['imageview1'].image = ui.Image('darkthunder.PNG')
if (a == 12):
	v['imageview1'].image = ui.Image('sunnyandcloud.PNG')
if (a == 2):
	v['imageview1'].image = ui.Image('darkandcloud.PNG')
if (a == 5) or (a == 14):
	v['imageview1'].image = ui.Image('darkcloud.PNG')
if (a == 1):
	v['imageview1'].image = ui.Image('dark.PNG')
if (a == 7):
	v['imageview1'].image = ui.Image('darkandrain.PNG')
if (a == 16):
	v['imageview1'].image = ui.Image('sunandrain.PNG')
if (a == 19) or (a == 10):
	v['imageview1'].image = ui.Image('mist.PNG')
if (a == 18) or (a == 9):
	v['imageview1'].image = ui.Image('snowy.PNG')
v['button2'].Button = ui.Button(title='OK')
v.present('sheet')
"""
notification.schedule("お天気をお知らせします", 3600, 'default','pythonista3://Wheather/Weather.py?action=run')
"""


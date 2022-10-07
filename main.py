from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_count2(start_date2):
  delta = today - datetime.strptime(start_date2, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_birthday2(birthday2):
  next = datetime.strptime(str(date.today().year) + "-" + birthday2, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days


def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2022-08-09')},"birthday_left":{"value":get_birthday2('05-20')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW8577rO31NJIf7irM7kP7TZc0', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2021-05-09')},"birthday_left":{"value":get_birthday2('01-08')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW852tpjVFdjClDI82TDmXY-Sw', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2019-07-20')},"birthday_left":{"value":get_birthday2('08-17')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW85xCASTUNV8aIMTQqtPmf49E', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2020-09-13')},"birthday_left":{"value":get_birthday2('08-16')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW85zaOCPUZLo_vntFktBX5xDg', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2022-03-19')},"birthday_left":{"value":get_birthday2('12-24')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW858sSM3YDLXIwwkgq1S7y_Tw', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2022-06-08')},"birthday_left":{"value":get_birthday2('10-30')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW858UE3f4owXx9trYXa6paB2k', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2022-10-02')},"birthday_left":{"value":get_birthday2('03-27')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW857BFhC5nuBj5t7pbnT0ZxY8', template_id, data)
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count2('2021-12-25')},"birthday_left":{"value":get_birthday2('02-14')},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template('osRW856FkPYD05_F15QABG4gDF7Y', template_id, data)
print(res)

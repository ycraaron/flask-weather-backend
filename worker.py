import pyowm
import datetime
import logging
import threading
from utils.db_driver.mongo import MongoDbConnection

API_KEY = '765208a84ecefc076615a3aa50ad3ba6'
owm = pyowm.OWM(API_KEY)


class WeatherWorker(object):

    def __init__(self):
        self.dic_city = {
            'HK': 1819730,
            'SG': 1880252
        }
        self.db_conn = MongoDbConnection().get_conn()
        self.log = logging.getLogger('weather-logger')
        self.file_handler = ''
        self.init_logger()

    def init_logger(self):
        self.log.setLevel(logging.DEBUG)
        self.file_handler = logging.FileHandler('weather_worker.log')
        self.file_handler.setLevel(logging.DEBUG)
        self.log.addHandler(self.file_handler)

    def update_all_city(self):
        threading.Timer(30.0, self.update_all_city).start()
        for key in self.dic_city:
            city_id = self.dic_city[key]
            observation = owm.weather_at_id(city_id)
            weather = observation.get_weather()
            humidity = weather.get_humidity()
            temper = weather.get_temperature('celsius')
            time = datetime.datetime.now()
            ts = datetime.datetime.timestamp(time)
            dic_doc = {
                'temperature': temper,
                'humidity': humidity,
                'timestamp': ts
            }
            collection = self.db_conn[key]
            success = collection.insert_one(dic_doc).inserted_id
            if success:
                print(key + ' success at ' + time.strftime('%A, %d. %B %Y %I:%M%p'))
                self.log.info(key + ' weather updated at ' + time.strftime('%A, %d. %B %Y %I:%M%p'))
            else:
                print(key + ' fail at ' + time.strftime('%A, %d. %B %Y %I:%M%p'))
                self.log.error(key + ' fail to update at ' + time.strftime('%A, %d. %B %Y %I:%M%p'))

worker = WeatherWorker()
worker.update_all_city()
# HK ID: 1819730
# SG ID: 1880252



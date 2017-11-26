import datetime
import pymongo
from utils.db_driver.mongo import MongoDbConnection

mongo = MongoDbConnection()

ls_city = ['HK', 'SG']


def fetch_weather(pars={}):
    db_conn = mongo.get_conn()
    ls_result = []
    city = pars['city']
    str_msg_fail = ''
    dic_fail = {'confirmation': 'fail', 'message': str_msg_fail}

    if city is None or city not in ls_city:
        dic_fail['message'] = 'city not found in database'
        return dic_fail

    start = pars['start']
    end = pars['end']
    date_format = "%Y-%m-%dT%H:%M:%S"
    collection = db_conn[city]

    # deal with start and end date logic
    # if start is not provided, end is, find the weather info earlier than end time
    # if start is provided, end is not, find the weather info later than start time
    # if both are provided and start is earlier than end, find the weather info within the time range
    if start is not None:
        start_time = datetime.datetime.strptime(start, date_format)
        start_ts = datetime.datetime.timestamp(start_time)
        if end is not None:
            end_time = datetime.datetime.strptime(end, date_format)
            end_ts = datetime.datetime.timestamp(end_time)
            if start_ts > end_ts:
                dic_fail['message'] = 'end date should not be earlier than start date'
                return dic_fail
            result = collection.find({'timestamp': {"$gt": start_ts, "$lt": end_ts}}).sort('timestamp', pymongo.DESCENDING).limit(10)
        else:
            result = collection.find({'timestamp': {"$gt": start_ts}}).sort('timestamp', pymongo.DESCENDING).limit(10)
    else:
        if end is not None:
            end_time = datetime.datetime.strptime(end, date_format)
            end_ts = datetime.datetime.timestamp(end_time)
            result = collection.find({'timestamp': {"$lt": end_ts}}).sort('timestamp', pymongo.DESCENDING).limit(10)
        else:
            result = collection.find().sort('timestamp', pymongo.DESCENDING).limit(10)

    dic_success = {'confirmation': 'success', 'weather': ls_result}
    for temp in result:
        dic = {'temperature': temp['temperature']['temp'], 'humidity': temp['humidity'], 'ts': temp['timestamp']}
        ls_result.append(dic)

    if len(dic_success['weather']) == 0:
        return []
    else:
        return dic_success


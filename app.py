from flask import Flask, request, jsonify, abort
from weather import fetch_weather

# __name__ help determine the root path
app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def weather():
    args = request.args
    msg_fail = ''
    dic_fail = {'confirmation': 'fail', 'message': msg_fail}

    # check number of parameters in get request
    if len(args) > 3:
        dic_fail['message'] = 'parameters exceed 3'
        return jsonify(dic_fail)

    # get all the key value of parameters
    keys = args.keys()
    dic_pars = {'city': None, 'start': None, 'end': None}

    # check city
    if 'city' in keys:
        city = args['city']
        dic_pars['city'] = city
    else:
        dic_fail['message'] = 'city not found'
        return jsonify(dic_fail)

    # check start and end time
    if 'start' in keys:
        start = args['start']
        dic_pars['start'] = start
    if 'end' in keys:
        end = args['end']
        dic_pars['end'] = end

    result = fetch_weather(dic_pars)

    if result:
        return jsonify(result)
    else:
        return jsonify({'confirmation': 'success', 'weather': 'no weather data available'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

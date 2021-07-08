import flask
from flask import request, jsonify

app = flask.Flask(__name__)

stations = [
    {
        'Name': 'bridge',
        'Address': '67 Eglinton Street, Glasgow, G5 9NR',
        'Facilities': 'Parking, Bike Shelter',
        'Nearby': 'Citizen’s Theatre, 02 Academy, Bike Hire.'

    },
    {
        'Name': 'buchanan street',
        'Address': '174 Buchanan Street, Glasgow, G1 2JZ',
        'Nearby': 'Queens Street Station, Buchanan Bus Station, Buchanan Galleries, Bike Hire.'

    }
]


@app.route('/', methods=['GET'])
def nopath():
    return 'Why hello there!'

@app.route('/all', methods=['GET'])
def all_stations():
    return jsonify(stations)


@app.route('/station', methods=['GET'])
def single_station():

    #Check if a station was present in the URL 
    if 'name' in request.args:
        name = str(request.args['name'])

    result=[]

    for s in stations:
        if s['Name'] == name:
            result.append(s)
            break
    
    return jsonify(result)



app.run(debug=True, host='0.0.0.0')



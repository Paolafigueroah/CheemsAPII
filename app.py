from flask import Flask, jsonify
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
def get_trips():
    trips = Trip.get()
    return trips  # Convierte la lista de diccionarios en JSON

@app.route('/trips', methods=['POST'])
def save_trip():
    data = request.json
    trip = Trip(name=data['name'], city=data['city'], country=data['country'])
    id = Trip.save(trip)
    success = id is not None
    return jsonify(success), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

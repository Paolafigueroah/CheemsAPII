from flask import Flask, request, jsonify
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
def trips():
    trips = Trip.get()
    return jsonify(trips)

@app.route('/trips', methods = ['POST'])
def save_trip():
    data = request.get_json()
    trip = Trip(name=data['name'], city = data['city'], country = data['country'], latitude = data['latitude'], longitude = data['longitude'])
    id = Trip.save(trip)
    success = id is not None
    return jsonify(success), 201

@app.route('/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    data = request.get_json()
    trip = Trip(name=data['name'], city=data['city'], country=data['country'], latitude = data['latitude'], longitude = data['longitude'])
    success = Trip.update(trip_id, trip)
    return jsonify(success), 200 if success else 404

@app.route('/trips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    success = Trip.delete(trip_id)
    return jsonify(success), 200 if success else 404

@app.route('/trips/<int:trip_id>', methods=['GET'])
def get_trip(trip_id):
    trip = Trip.get_by_id(trip_id)
    if trip:
        return jsonify(trip)
    return jsonify({"error": "Trip no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
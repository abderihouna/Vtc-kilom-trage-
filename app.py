from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
@app.route('/api/trips', methods=['POST'])
def add_trip():
    data = request.get_json()
    return jsonify({'status': 'Trajet ajouté'}), 201
    @app.route('/api/reports/export', methods=['GET'])
def export_report(): 
    return jsonify({'status': 'Rapport généré'}), 200

@app.route('/api/trips', methods=['GET'])
def get_trips():
    return jsonify({'status': 'Trajets récupérés'}), 200
@app.route('/api/trips/<id>', methods=['DELETE'])
def delete_trip(id):
def get_trip(id):
    return jsonify({'status': 'Trajet récupéré'}), 200





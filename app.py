#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance, Occupation, Group

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to the API!'

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    print("Received data:", data)  # Debugging output

    if not data or not all(k in data for k in ("rating", "episode_id", "guest_id")):
        return jsonify({"error": "Invalid data"}), 400

    new_appearance = Appearance(rating=data['rating'], episode_id=data['episode_id'], guest_id=data['guest_id'])
    
    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({"message": "Appearance created", "appearance": data}), 201

# Add a new route for retrieving an episode by ID
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    # Assuming Episode model has a `to_dict()` method that serializes the data
    return jsonify(episode.to_dict()), 200
@app.route('/episodes', methods=['GET'])
def get_all_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)

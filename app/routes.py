from flask import jsonify, request
from .models import db, Episode, Guest, Appearance
from .schemas import EpisodeSchema, GuestSchema, AppearanceSchema

episode_schema = EpisodeSchema(many=True)
guest_schema = GuestSchema(many=True)
appearance_schema = AppearanceSchema()

def init_routes(app):
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Podcast API!",
            "endpoints": {
                "/episodes": "Get all episodes",
                "/episodes/<int:id>": "Get a specific episode by ID",
                "/guests": "Get all guests",
                "/appearances": "Create a new appearance (POST)"
            }
        })

    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        return episode_schema.dump(episodes)

    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        episode = Episode.query.get(id)
        if episode is None:
            return jsonify({"error": "Episode not found"}), 404
        return episode_schema.dump(episode)

    @app.route('/guests', methods=['GET'])
    def get_guests():
        guests = Guest.query.all()
        return guest_schema.dump(guests)

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        errors = appearance_schema.validate(data)
        if errors:
            return jsonify({"errors": errors}), 400

        try:
            appearance = Appearance(rating=data['rating'], episode_id=data['episode_id'], guest_id=data['guest_id'])
            db.session.add(appearance)
            db.session.commit()
            return appearance_schema.dump(appearance), 201
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

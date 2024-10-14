from marshmallow import Schema, fields

class EpisodeSchema(Schema):
    id = fields.Int()
    date = fields.Str()
    number = fields.Int()

class GuestSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    occupation = fields.Str()

class AppearanceSchema(Schema):
    id = fields.Int()
    rating = fields.Int()
    episode_id = fields.Int()
    guest_id = fields.Int()
    episode = fields.Nested(EpisodeSchema)
    guest = fields.Nested(GuestSchema)

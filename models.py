from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

# Define metadata for naming conventions
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
})

# Initialize the SQLAlchemy instance
db = SQLAlchemy(metadata=metadata)

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    number = Column(Integer, unique=True, nullable=False)

    # Relationship to Appearance
    appearances = relationship('Appearance', backref='episode')

    # Exclude recursive references when serializing
    serialize_rules = ('-appearances.episode',)

    def __init__(self, date, number):
        self.date = date
        self.number = number

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    occupation = Column(String)

    # Relationship to Appearance
    appearances = relationship('Appearance', backref='guest')

    # Exclude recursive references when serializing
    serialize_rules = ('-appearances.guest',)

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    episode_id = Column(Integer, ForeignKey('episodes.id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('guests.id'), nullable=False)

    # Relationship to Episode and Guest
    episode = relationship('Episode', backref='appearance_list')
    guest = relationship('Guest', backref='appearance_list')

    # Exclude recursive references when serializing
    serialize_rules = ('-episode.appearance_list', '-guest.appearance_list')

    def __init__(self, rating, episode_id, guest_id):
        self.rating = rating
        self.episode_id = episode_id
        self.guest_id = guest_id

# Add the new models for Occupation and Group if applicable
class Occupation(db.Model, SerializerMixin):
    __tablename__ = 'occupations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to Guest
    guests = relationship('Guest', backref='occupation')

    def __init__(self, name):
        self.name = name

class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship to Guest
    guests = relationship('Guest', backref='group')

    def __init__(self, name):
        self.name = name

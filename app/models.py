from app import db


class Faction(db.Model):

    __tablename__ = 'factions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    army_id = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, name, army_id):
        self.name = name
        self.army_id = army_id

    def __repr__(self):
        return '<Faction %r>' % self.name

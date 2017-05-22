from flask import render_template

from app import app
from app.models import Faction


@app.route('/')
def index():
    factions = Faction.query.all()
    return render_template('index.html', factions=factions)


@app.route('/faction/<int:army_id>')
def faction(army_id):
    faction = Faction.query.filter_by(army_id=army_id).one()
    return render_template('faction.html', faction=faction)

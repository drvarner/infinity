import lzstring

from flask import render_template, request

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


@app.route('/armyCode/<code>', methods=['GET', 'POST'])
def armyCode(code):
    decoded = lzstring.LZString().decompressFromBase64(code).split('|')

    faction = Faction.query.filter_by(army_id=decoded[0]).one()
    groups = breakGroups(decoded[3])
    units = []

    for group in groups:
        units.append(group.split('!'))

    units.pop()
    units.pop()

    armyList = {
        'Title': decoded[2],
        'Points': decoded[1],
        'Units': units
    }

    return render_template(
        'code_info.html',
        armyList=armyList,
        faction=faction
    )


def breakGroups(code, splitstring='@'):
    return code.split(splitstring)

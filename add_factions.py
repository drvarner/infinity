from app import db
from app.models import Faction

pano = Faction(101, 'PanOceania')
haqq = Faction(401, 'Haqqislam')

db.session.add(pano)
db.session.add(haqq)
db.session.commit()

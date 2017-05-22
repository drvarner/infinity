from app import db
from app.models import Faction

pano = Faction('PanOceania', 101)
yuji = Faction('Yu Jing', 201)
aria = Faction('Ariadna', 301)
haqq = Faction('Haqqislam', 401)
noma = Faction('Nomads', 501)
comb = Faction('Combined Army', 601)
alep = Faction('Aleph', 701)
toha = Faction('Tohaa', 801)

db.session.add(pano)
db.session.add(yuji)
db.session.add(aria)
db.session.add(haqq)
db.session.add(noma)
db.session.add(comb)
db.session.add(alep)
db.session.add(toha)
db.session.commit()

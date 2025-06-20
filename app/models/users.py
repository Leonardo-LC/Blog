from app import db
from datetime import datetime

#modelo d
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #significa um "id" e ele assina só
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r' % self.name
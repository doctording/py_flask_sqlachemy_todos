# db = SQLAlchemy(app)
from web import db

class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, sno, password):
        self.sno = sno
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.sno
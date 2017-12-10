
# db = SQLAlchemy(app)
from web import db

class Todo(db.Model):
    __tablename__ = 't_todo'
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(255))
    task = db.Column(db.Text)
    finish = db.Column(db.Integer)
    createtime = db.Column(db.DateTime)

    def __init__(self, sno, task, finish, createtime):
        self.sno = sno
        self.task = task
        self.finish = finish
        self.createtime = createtime

    def __repr__(self):
        return '<Todo %r>' % self.id
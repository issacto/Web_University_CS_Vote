from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    comment = db.Column(db.String(100),nullable = True)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'

from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.String, unique=False, nullable=False)
    start_time = db.Column(db.String, unique=False, nullable=False)
    execution_time = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '%s, %s, %s' % (self.create_time, self.start_time, self.execution_time)

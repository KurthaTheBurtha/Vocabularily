from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    score = db.Column(db.String(20), index=True, unique = False)

    def __repr__(self):
        return '{}: {}'.format(self.username,self.score)
from ..database import db

class Writer(db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='writer', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [book.serialize() for book in self.books]
        }
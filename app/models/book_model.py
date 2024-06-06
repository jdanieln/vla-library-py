from ..database import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'), nullable=False)
    loans = db.relationship('Loan', backref='book', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'writer_id': self.writer_id
        }
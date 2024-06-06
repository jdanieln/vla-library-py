from ..database import db

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    loans = db.relationship('Loan', backref='member', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'loans': [loan.serialize() for loan in self.loans]
        }
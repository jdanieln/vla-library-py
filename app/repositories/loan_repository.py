from .base_repository import BaseRepository
from ..models.loan_model import Loan
from ..database import db

class LoanRepository(BaseRepository):

    def get_all(self):
        return Loan.query.all()

    def get_by_id(self, loan_id):
        return Loan.query.get(loan_id)

    def create(self, loan):
        db.session.add(loan)
        db.session.commit()

    def delete(self, loan_id):
        loan = Loan.query.get(loan_id)
        if loan:
            db.session.delete(loan)
            db.session.commit()
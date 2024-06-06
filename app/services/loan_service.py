from ..models.loan_model import Loan

class LoanService:
    def __init__(self, loan_repository):
        self.loan_repository = loan_repository
    
    def get_all_loans(self):
        return self.loan_repository.get_all()
    
    def get_loan_by_id(self, loan_id):
        return self.loan_repository.get_by_id(loan_id)
    
    def create_loan(self, data):
        new_loan = Loan(name=data['name'])
        self.loan_repository.create(new_loan)
    
    def delete_loan(self, loan_id):
        self.loan_repository.delete(loan_id)
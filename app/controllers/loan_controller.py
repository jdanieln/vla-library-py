from flask import Blueprint, request, jsonify
from ..services.loan_service import LoanService
from flask_jwt_extended import jwt_required

def create_loan_blueprint(loan_service: LoanService):
    loan_blueprint= Blueprint('loan', __name__)

    @loan_blueprint.route('/loans', methods=['GET'])
    @jwt_required()
    def get_all_loans():
        loans = loan_service.get_all_loans()
        return jsonify([loan.serialize() for loan in loans])

    @loan_blueprint.route('/loan/<int:loan_id>', methods=['GET'])
    def get_loan_by_id(loan_id):
        loan = loan_service.get_loan_by_id(loan_id)
        if loan:
            return jsonify([loan.serialize()])
        return jsonify({"message":'Loan not found'}),404

    @loan_blueprint.route('/loan/<int:loan_id>', methods=['POST'])
    def create_loan():
        data=request.get_json()
        loan_service.create_loan(data)
        return jsonify({"message": 'Loan created successfully'}), 201

    @loan_blueprint.route('/loan/<int:loan_id>', methods=['DELETE'])
    def delete_write(loan_id):
        loan_service.delete_write(loan_id)
        return jsonify({"message": 'Loan deleted successfully'}), 200
    
    return loan_blueprint
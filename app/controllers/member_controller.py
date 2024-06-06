from flask import Blueprint, request, jsonify
from ..services.member_service import MemberService

def create_member_blueprint(member_service: MemberService):
    member_blueprint= Blueprint('member', __name__)

    @member_blueprint.route('/members', methods=['GET'])
    def get_all_members():
        members = member_service.get_all_members()
        return jsonify([member.serialize() for member in members])

    @member_blueprint.route('/member/<int:member_id>', methods=['GET'])
    def get_member_by_id(member_id):
        member = member_service.get_member_by_id(member_id)
        if member:
            return jsonify([member.serialize()])
        return jsonify({'message': 'Member not found'}), 404

    @member_blueprint.route('/member/<int:member_id>', methods=['POST'])
    def create_member():
        data=request.get_json()
        member_service.create_member(data)
        return jsonify({"message": 'Member created successfully'}), 201

    @member_blueprint.route('/member/<int:member_id>', methods=['DELETE'])
    def delete_write(member_id):
        member_service.delete_write(member_id)
        return jsonify({"message": 'Member deleted successfully'}), 200
    
    return member_blueprint
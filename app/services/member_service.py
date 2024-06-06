from ..models.member_model import Member

class MemberService:
    def __init__(self, member_repository):
        self.member_repository = member_repository

    def get_all_members(self):
        return self.member_repository.get_all()
    
    def get_member_by_id(self, member_id):
        return self.member_repository.get_by_id(member_id)
    
    def create_member(self, data):
        new_member = Member(name=data['name'])
        self.member_repository.create(new_member)

    def delete_member(self, member_id):
        self.member_repository.delete(member_id)
    
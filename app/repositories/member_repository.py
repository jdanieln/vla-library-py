from .base_repository import BaseRepository
from ..models.member_model import Member
from ..database import db

class MemberRepository(BaseRepository):

    def get_all(self):
        return Member.query.all()
    
    def get_by_id(self, member_id):
        return Member.query.get(member_id)
    
    def create(self, member):
        db.session.add(member)
        db.session.commit()

    def delete(self, member_id):
        member = Member.query.get(member_id)
        if member:
            db.session.delete(member_id)
            db.session.commit()
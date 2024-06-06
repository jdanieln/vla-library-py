from .base_repository import BaseRepository
from ..models.writer_model import Writer
from ..database import db

class WriterRepository(BaseRepository):
    def get_all(self):
        return Writer.query.all()

    def get_by_id(self, writer_id):
        return Writer.query.get(writer_id)

    def create(self, writer):
        db.session.add(writer)
        db.session.commit()

    def delete(self, writer_id):
        writer = Writer.query.get(writer_id)
        if writer:
            db.session.delete(writer)
            db.session.commit()
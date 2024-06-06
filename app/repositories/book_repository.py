from .base_repository import BaseRepository
from ..models.book_model import Book
from ..database import db

class BookRepository(BaseRepository):
    
    def get_all(self):
        return Book.query.all()

    def get_by_id(self, book_id):
        return Book.query.get(book_id)
    
    def create(self, book):
        db.session.add(book)
        db.session.commit()

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
    
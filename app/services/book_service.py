from ..models.book_model import Book

class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def get_all_books(self):
        return self.book_repository.get_all()

    def get_book_by_id(self, book_id):
        return self.book_repository.get_by_id(book_id)
    
    def create_book(self, data):
        new_book = Book(title=data['title'], writer_id=data['writer_id'])
        self.book_repository.create(new_book)

    def delete_book(self, book_id):
        self.book_repository.delete(book_id)
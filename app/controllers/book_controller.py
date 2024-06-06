from flask import Blueprint, request, jsonify
from ..services.book_service import BookService

def create_book_blueprint(book_service: BookService):
    book_blueprint= Blueprint('book', __name__)

    @book_blueprint.route('/books', methods=['GET'])
    def get_all_books():
        books = book_service.get_all_books()
        return jsonify([book.serialize() for book in books])

    @book_blueprint.route('/book/<int:book_id>', methods=['GET'])
    def get_book_by_id(book_id):
        book = book_service.get_book_by_id(book_id)
        if book:
            return jsonify([book.serialize()])
        return jsonify({'message': 'Book not found'}), 404

    @book_blueprint.route('/book/<int:book_id>', methods=['POST'])
    def create_book():
        data=request.get_json()
        book_service.create_book(data)
        return jsonify({"message": 'Book created successfully'}), 201

    @book_blueprint.route('/book/<int:book_id>', methods=['DELETE'])
    def delete_write(book_id):
        book_service.delete_write(book_id)
        return jsonify({"message": 'Book deleted successfully'}), 200
    
    return book_blueprint
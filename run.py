from app import create_app
from app.controllers.book_controller import create_book_blueprint
from app.controllers.writer_controller import create_writer_blueprint
from app.controllers.member_controller import create_member_blueprint
from app.controllers.loan_controller import create_loan_blueprint
from app.repositories.book_repository import BookRepository
from app.repositories.writer_repository import WriterRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.loan_repository import LoanRepository
from app.services.book_service import BookService
from app.services.writer_service import WriterService
from app.services.member_service import MemberService
from app.services.loan_service import LoanService


from flask_migrate import Migrate
from app.database import db

app = create_app()

book_repository = BookRepository()
book_service = BookService(book_repository)

writer_repository = WriterRepository()
writer_service = WriterService(writer_repository)

loan_repository = LoanRepository()
loan_service = LoanService(loan_repository)

member_repository = MemberRepository()
member_service = MemberService(member_repository)

app.register_blueprint(create_book_blueprint(book_service), url_prefix='/api')
app.register_blueprint(create_writer_blueprint(writer_service), url_prefix='/api')
app.register_blueprint(create_loan_blueprint(loan_service), url_prefix='/api')
app.register_blueprint(create_member_blueprint(member_service), url_prefix='/api')

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
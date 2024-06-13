from app import create_app
from app.controllers.book_controller import create_book_blueprint
from app.controllers.writer_controller import create_writer_blueprint
from app.controllers.member_controller import create_member_blueprint
from app.controllers.loan_controller import create_loan_blueprint
from app.controllers.auth_controller import auth_blueprint
from app.repositories.book_repository import BookRepository
from app.repositories.writer_repository import WriterRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.loan_repository import LoanRepository
from app.services.book_service import BookService
from app.services.writer_service import WriterService
from app.services.member_service import MemberService
from app.services.loan_service import LoanService
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint


from flask_migrate import Migrate
from app.database import db

app = create_app()
jwt = JWTManager(app)

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
app.register_blueprint(auth_blueprint, url_prefix='/auth')

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': 'Biblioteca API VLA'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()

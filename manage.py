from flask.cli import FlaskGroup
from app import create_app
from app.database import db
from flask_migrate import Migrate

app = create_app()
cli = FlaskGroup(create_app=create_app)
migrate = Migrate(app, db)

if __name__ == 'main':
    cli()
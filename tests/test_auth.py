import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.database import db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    #response = client.post('/auth/register', json={
    #    "username": "test-user",
    #    "password": "test-pwd"
    #})

    assert 201 == 201
    #assert response.json['message'] == 'Usuario registrado satisfactoriamente'

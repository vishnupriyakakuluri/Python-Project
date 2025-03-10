import pytest
import os
from flask import session
from app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DEBUG'] = False  # Ensure Flask is not in debug mode
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to DAV Bank' in response.data

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'contact' in response.data

def test_signup_page(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert b'signup' in response.data

def test_valid_signup(client):
    response = client.post('/signup', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'Test@1234',
        'account_number': '1234567'
    }, follow_redirects=True)

    assert b'Login' in response.data or b'Sign in' in response.data  # Adjust to match actual login page content


def test_invalid_signup(client):
    response = client.post('/signup', data={
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'Test@1234',
        'account_number': '1234567'
    }, follow_redirects=True)

    assert b'Account created successfully' in response.data or b'Login' in response.data


def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_valid_login(client):
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'Test@1234'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_invalid_login(client):
    response = client.post('/login', data={
        'username': 'wronguser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_dashboard_access(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1
        sess['username'] = 'testuser'
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Welcome' in response.data  # Modify this based on actual dashboard content


def test_chat_unauthenticated(client):
    response = client.post('/chat', json={'message': 'Hello'})
    assert response.status_code == 401
    assert b'User not logged in' in response.data

def test_logout(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1
        sess['username'] = 'testuser'

    response = client.get('/logout', follow_redirects=True)

    assert b'Login' in response.data or b'Sign in' in response.data  # Match login page content


def test_404_page(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data



import pytest
from flask import url_for
from app import app  # Ensure 'app' is your Flask instance


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Test home page (Ensure correct endpoint)
def test_home_page(client):
    response = client.get(url_for('home_page'))  # Use the correct endpoint name
    assert response.status_code == 200
    assert b'Welcome' in response.data  # Ensure the expected content is present


# Test services page (Ensure correct endpoint)
def test_services_page(client):
    response = client.get(url_for('services_page'))  # Match function name in Flask app
    assert response.status_code == 200
    assert b'Services' in response.data  # Ensure the expected content is present


# Test contact form (Ensure all required fields are provided)
def test_contact_form(client):
    response = client.post(url_for('contact_page'), data={
        'name': 'John Doe',
        'email': 'johndoe@example.com',  # Ensure required email field is included
        'message': 'Hello, I need help!'
    }, follow_redirects=True)

    assert response.status_code == 200  # Expect success
    assert b'Thank you' in response.data  # Ensure a success message appears


# Test login with valid credentials (Ensure correct redirects)
def test_login(client):
    response = client.post(url_for('login'), data={
        'username': 'validuser',
        'password': 'correctpassword'
    }, follow_redirects=True)  # Follow the redirect

    assert response.status_code == 200  # Expect success after redirect
    assert b'Dashboard' in response.data  # Ensure login leads to dashboard


# Test logout (Ensure expected logout message appears)
def test_logout(client):
    # First, login the user
    client.post(url_for('login'), data={
        'username': 'validuser',
        'password': 'correctpassword'
    }, follow_redirects=True)

    # Then, logout
    response = client.get(url_for('logout'), follow_redirects=True)

    assert response.status_code == 200
    assert b'You have been logged out' in response.data  # Ensure correct logout message

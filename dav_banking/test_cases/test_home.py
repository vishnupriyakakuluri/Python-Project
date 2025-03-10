import pytest
from flask import Flask
from app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to DAV Bank" in response.data
    assert b"Your trusted partner for financial growth" in response.data

def test_login_route(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data  # Assuming 'Login' is in the login page

def test_signup_route(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert b"Sign Up" in response.data  # Assuming 'Sign Up' is in the signup page

def test_services_route(client):
    response = client.get('/services')
    assert response.status_code == 200
    assert b"Services" in response.data  # Assuming 'Services' is in the services page

def test_contact_route(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact Us" in response.data  # Assuming 'Contact Us' is in the contact page

def test_banner_content(client):
    response = client.get('/')
    assert b"Experience Banking Like Never Before" in response.data
    assert b"Join us for secure, fast, and reliable banking services tailored to your needs." in response.data

def test_features_content(client):
    response = client.get('/')
    assert b"Secure Transactions" in response.data
    assert b"24/7 Customer Support" in response.data
    assert b"Easy Online Access" in response.data
    assert b"Personalized Insights" in response.data

def test_footer_content(client):
    response = client.get('/')
    assert b"&copy; 2025 DAV Bank. All rights reserved." in response.data
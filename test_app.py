from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_ping():
    client = app.test_client()
    response = client.get('/ping')
    data = response.get_json()
    assert data['message'] == 'pong!'
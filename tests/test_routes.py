from app import *

client = app.test_client()

def test_base_route():
    response = client.get('/')
    assert response.status_code == 200
    assert b"This is my manager for event logs" in response.data

    
def test_create():
    response = client.get('/create')
    assert response.status_code == 200
    assert b"This is my manager for event logs on the Active Directory" in response.data
    
def test_about():
    response = client.get('/about')
    assert response.status_code == 200
    assert  b"Just a CRUD web app for event logs!" in response.data



if __name__ == "__main__":
    app.main()
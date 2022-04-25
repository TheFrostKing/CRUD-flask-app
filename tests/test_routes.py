from flask import Flask


from app import *
client = app.test_client()

def test_base_route():

    assert client.get('/').status_code == 200
    
def test_create():
    assert client.get('/create').status_code == 200
    
def test_about():
    assert client.get('/about').status_code == 200


if __name__ == "__main__":
    test_about()
    test_create()
    test_base_route()
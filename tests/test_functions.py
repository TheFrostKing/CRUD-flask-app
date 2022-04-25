from flask import Flask
from app import *

client = app.test_client()

def test_create_func():
    assert client.post('/create', data={'level': 'TEST', 'date_time': '2021-04-25T10:00', 'source': 'TEST', 'event_id': '4444' }).status_code==200
def test_delete_func():
    assert client.get('/data/999/delete').status_code == 401
def test_update():
    
    assert client.post('/data/4/update').status_code == 200

def test_search():
    assert client.post('/search').status_code == 200


if __name__ == "__main__":
    test_create_func()
    test_delete_func()
    test_search()
    test_update()

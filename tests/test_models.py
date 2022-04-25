from app import *


# I removed some config passing here
def create_app():
    db.create_all()

def setUp():

    db.create_all()

def tearDown():

    db.session.remove()
    db.drop_all()


create_app()
from flask import Flask
from models import db

from handler.routes import configure_routes

# create an instance of the flask app
app = Flask(__name__)

# database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()
        
configure_routes(app)
 
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(ssl_context=('self_signed/cert.pem', 'self_signed/key.pem'), host ="0.0.0.0", port=5000, debug = True)

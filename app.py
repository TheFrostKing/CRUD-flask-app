from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from models import db, Events_model, User
from datetime import datetime, timedelta
from flask_login import REFRESH_MESSAGE, UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from forms import RegisterForm, LoginForm

# create an instance of the flask app
app = Flask(__name__)
bcrypt = Bcrypt(app)
# database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ItShouldBeAnythingButSecret' 
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = (u"Session timed out, please re-login")
login_manager.needs_refresh_message_category = "info"

@app.before_first_request
def create_table():
    db.create_all()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1) # time for inactivity
    session.modified = True # refresh session of inactivity

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data) #hashing the passwd
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit(), 200
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=form,  name = current_user)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



''' FORM TO CREATE NEW DATA '''
@app.route('/create' , methods = ['GET','POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    

    if request.method == 'POST':
        level = request.form['level']
        date_time = request.form['date_time']
        datetime_object = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
        source = request.form['source']
        event_id = request.form['event_id']
        application_log = Events_model(level=level, date_time=datetime_object, source=source, event_id=event_id)
        db.session.add(application_log)
        db.session.commit()
        return redirect('/')

    return  'Failed to create'
            


''' SEARCH SINGLE ELEMENT'''

@app.route('/search', methods = ['POST']) # SOLO SEARCH
@login_required
def RetrieveLog():
    if request.method == "POST":
        id = request.form.get('id') 
        
        application_logs = Events_model.query.filter_by(id=id)
        if application_logs:
            return render_template('index.html', application_logs=application_logs), 200

    return render_template('index.html', application_logs=[])


@app.route('/data/<int:id>', methods = ['GET', 'POST'])
@login_required
def RetrieveSingleEmployee(id):
    application_log = Events_model.query.filter_by(id=id).first()
    if application_log: 
        return render_template('data.html', application_log = application_log)
    return f"ID with id ={id} Doesn't exist", 404


''' UPDATE EXISTING DATA'''

@app.route('/data/<int:id>/update',methods = ['GET','POST'])
@login_required
def update(id):
    application_log = Events_model.query.filter_by(id=id).first()
    if request.method == 'POST':
        print(request.form)
        if application_log:
            application_log.level = request.form['level']
            date_time = request.form['date_time']              
            application_log.date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
            application_log.source = request.form['source']
            application_log.event_id = request.form['event_id']

            db.session.add(application_log)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"error with id ={id} Doesn't exist", 200

    return render_template('update.html', application_log = application_log)
    

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
@login_required   
def delete(id):
    application_log = Events_model.query.filter_by(id=id).first()
    if request.method == 'GET':
        if application_log:
            db.session.delete(application_log)
            db.session.commit()
            return redirect('/')
        return 'Failed to delete', 401
    return redirect('/')


@app.route('/')
@login_required
def home():
    application_logs = Events_model.query.all()
    return render_template('index.html', application_logs=application_logs, name = current_user), 200

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html'),200



if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(ssl_context=('self_signed/cert.pem', 'self_signed/key.pem'), host ="0.0.0.0", port=5000, debug = True)

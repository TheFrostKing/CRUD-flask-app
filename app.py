# import packages
from email.mime import application
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Application_Error
 

# create an instance of the flask app
app = Flask(__name__)

# database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        level = request.form['level']
        date_time = request.form['date_time']
        source = request.form['source']
        event_id = request.form['event_id']
        application_log = Application_Error(level=level, date=date_time, source=source, event_id=event_id)
        db.session.add(application_log)
        db.session.commit()
        return redirect(url_for('data'))
    
    


@app.route('/data')
def RetrieveList():
    application_logs = Application_Error.query.all()
    return render_template('datalist.html',application_logs = application_logs)


# @app.route('/data/<str:id>') # SOLO SEARCH
# def RetrieveLog(id):
#     application_log = Application_Error.query.filter_by(level=id).first()
#     if application_log:
#         return render_template('data.html', employee = application_log)
#     return f"Employee with id ={id} Doesn't exist"
 

# @app.route('/data/<string:level>/update',methods = ['GET','POST'])
# def update(id):
#     application_log = Application_Error.query.filter_by(level=id).first()
#     if request.method == 'POST':
#         if application_log:
#             db.session.delete(application_log)
#             db.session.commit()
 
#             level = request.form['level']
#             date_time = request.form['date_time']
#             source = request.form['source']
#             event_id = request.form['event_id']
#             application_log = Application_Error(level=level, date=date_time, source=source, event_id = event_id)
 
#             db.session.add(application_log)
#             db.session.commit()
#             return redirect(f'/data/{id}')
#         return f"Employee with id = {id} Does not exist"
 
#     return render_template('update.html', application_log = application_log)

 
app.run(host='localhost', port=5000)

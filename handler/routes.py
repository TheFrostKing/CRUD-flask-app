from flask import Flask, render_template, request, redirect
from models import db, Events_model
from datetime import datetime

def configure_routes(app):
    ''' FORM TO CREATE NEW DATA '''
    @app.route('/create' , methods = ['GET','POST'])
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
            return redirect('/'), 200

        return  'Failed to create', 401
            


    ''' SEARCH SINGLE ELEMENT'''

    @app.route('/search', methods = ['POST']) # SOLO SEARCH
    def RetrieveLog():
        if request.method == "POST":
            id = request.form.get('id') 
            
            application_logs = Events_model.query.filter_by(id=id)
            if application_logs:
                return render_template('index.html', application_logs=application_logs), 200

        return render_template('index.html', application_logs=[])
    

    @app.route('/data/<int:id>', methods = ['GET', 'POST'])
    def RetrieveSingleEmployee(id):
        application_log = Events_model.query.filter_by(id=id).first()
        if application_log: 
            return render_template('data.html', application_log = application_log)
        return f"ID with id ={id} Doesn't exist", 404


    ''' UPDATE EXISTING DATA'''

    @app.route('/data/<int:id>/update',methods = ['GET','POST'])
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
    def delete(id):
        application_log = Events_model.query.filter_by(id=id).first()
        if request.method == 'GET':
            if application_log:
                db.session.delete(application_log)
                db.session.commit()
                return redirect('/'), 200
            return 'Failed to delete', 401
        return redirect('/')



    @app.route('/')
    def home():
        application_logs = Events_model.query.all()
        return render_template('index.html', application_logs=application_logs), 200

    @app.route('/about')
    def about():
        return render_template('about.html'),200
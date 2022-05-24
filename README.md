# CRUD project 
 CRUD web application using the FLASK framework. 

# What it does?
The purpose of this project is to monitor event logs from different Windows Servers either remotely or locally. The file `get_logs.py` is a script which filters windows event logs and sends them to a database where a Flask application has CRUD functionality on the database:
> Create your own events. <br>
> Search by unique ID.<br>
> Read filtered events and get information about their source, status, time, etc.<br>
> Delete events.

The database used is SQLite together with its toolkit SqlAlchemy.
It gets data every 24 hours by a script that takes the logs from the Windows Event Viewer and executes queries into the DB.
Connection happens over HTTPS with self-signed certificates.

# Docker and how to run the app?
The application is ready to be ran with docker. You either build the image yourself with the Dockerfile or use the ready to download image available on Docker Hub - https://hub.docker.com/repository/docker/altrosvet/crud_app/. It is configured to work with Gunicorn WSGI. <br>`run -it -p 443:443 --network host app` will run it on local addresses make sure port 443 is open for https connection. <br>
Another way of running the app is to just use the Flask WSGI, by simply running it with  `flask run --cert self_signed/cert.pem --key self_signed/key.pem -h 0.0.0.0`

# Security concerns
The application provides login functionality using `Flask-logins`. All the passwords are hashed and salted in the database. The scenario which I developed it uses `Flask-Admin`, an alternative Flask  to phpMyAdmin, because users are meant to be SysOps and they are supposed to recieve company accounts not create their own. Although, I left a registration form, which could be returned or removed at any time. <br>
Furthermore, I decided to generate my own self-signed certificates so the application is running with already predefined ones, users have to add them to their browser. The connection happens under HTTP.<br>
In addition, `Flask-Talisman` is used to forces all connects to https and it is important to update the list in the beggining of the code if any external resources are used, in the HTML for e.g. 


# Libraries and frameworks.
>pywin32 <br>
>SqlAlchemy<br>
>Flask<br>
>flask_sqlchemy<br>
>Flask_Login<br>
>Flask-Admin<br>
>Flask-Talisman

# Overview
![flask scheme](https://user-images.githubusercontent.com/37861327/164088467-0ccaf220-7fde-4fcb-8b79-e5e5fe333228.png)

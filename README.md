# CRUD project 
 CRUD web application using the FLASK framework. 

# The database
I am using SQLite and SQLAlchemy.
The database gets gets data every 24 hours by a script that takes the logs from the Windows Event Viewer and executes queries into SQLite DB.
Connection happens over HTTPS with self-signed certificates.

# Libraries used
>pywin32 <br>
>SqlAlchemy <br>
>openssl

# Sources I used and inspired me
>https://sejalrawat25.medium.com/creating-a-crud-application-with-flask-19c18ff128b5
>https://www.accadius.com/using-python-read-windows-event-logs-multiple-servers/

# Overview
![flask scheme](https://user-images.githubusercontent.com/37861327/164088467-0ccaf220-7fde-4fcb-8b79-e5e5fe333228.png)

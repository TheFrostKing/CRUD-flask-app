# syntax=docker/dockerfile:1

FROM python:3.10.0

EXPOSE 5000
EXPOSE 443

WORKDIR /flask_crud

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /flask_crud

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
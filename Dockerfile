FROM python:3.8

WORKDIR /usr/src
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#COPY . .

CMD ["flask", "run"]
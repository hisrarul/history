FROM python:3.9
WORKDIR /code
ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
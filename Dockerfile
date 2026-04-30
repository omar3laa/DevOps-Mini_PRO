FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask

RUN pip install mysql-connector-python

CMD ["python", "app.py"]
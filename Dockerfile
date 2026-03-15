FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 9000

CMD ["python3","app.py"]


FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask mysql-connector-python

COPY app.py /app/app.py

CMD ["python", "app.py"]

FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask mysql-connector-python prometheus_flask_exporter

COPY app.py /app/app.py

CMD ["python", "app.py"]

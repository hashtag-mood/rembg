FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV FLASK_APP=app.py

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:80", "app:app"]
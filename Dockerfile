FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r tasks.txt

CMD ["python", "main.py"]

FROM python:3.12

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 8000

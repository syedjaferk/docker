FROM python:3.8-slim

LABEL owner="satheesh"
LABEL email="test@gmail.com"

WORKDIR /flaskapp2
WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt 
# Install required packages

COPY . .

ENV NAME="Jafer Default Value"

# Readibility
EXPOSE 5000

CMD ["python", "app.py"]

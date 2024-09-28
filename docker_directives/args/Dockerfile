ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}-slim

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

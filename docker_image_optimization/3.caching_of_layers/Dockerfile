FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 
ENV NAME="Jafer"
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

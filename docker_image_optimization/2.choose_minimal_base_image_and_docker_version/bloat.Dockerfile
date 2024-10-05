FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .

ENV NAME="Jafer"
EXPOSE 5000
CMD ["python", "app.py"]

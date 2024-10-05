FROM golang:1.21.0-alpine

WORKDIR /app

COPY app.go /app
CMD ["go", "run", "app.go"]



FROM golang:1.21.0-alpine
WORKDIR /app
COPY main.go /app
CMD ["go", "run", "main.go"]
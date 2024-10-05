FROM golang:1.21.0-alpine AS build
WORKDIR /app
COPY app.go .
RUN go build -o myapp app.go

FROM alpine:3.18
WORKDIR /app
COPY --from=build /app/myapp .
CMD ["./myapp"]

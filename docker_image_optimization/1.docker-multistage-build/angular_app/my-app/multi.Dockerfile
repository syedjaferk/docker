FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist/my-app/browser /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
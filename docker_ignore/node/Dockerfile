FROM node:20.17-slim

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm i

COPY index.js /app

CMD ["node", "index.js"]

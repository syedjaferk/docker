FROM node:20.13.1-alpine

WORKDIR /app

COPY index.js /app
COPY package.json /app
COPY package-lock.json /app

RUN npm i

CMD ["node", "index.js"]
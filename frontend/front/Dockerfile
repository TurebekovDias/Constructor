# syntax=docker/dockerfile:1

FROM node:22-alpine AS build
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build   # даёт dist/<proj>/browser

FROM node:22-alpine
ENV NODE_ENV=production
WORKDIR /app
RUN npm i -g serve@14

# копируем именно browser; wildcard подхватит имя проекта
COPY --from=build /usr/src/app/dist/*/browser/ ./

USER node
EXPOSE 4200
CMD ["serve", "-s", ".", "-l", "tcp://0.0.0.0:4200"]
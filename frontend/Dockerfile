FROM node:16 AS build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install

# Скопировать исходный код Vue.js
COPY . .

# Выполнить сборку
RUN npm run build

FROM nginx:stable-alpine AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

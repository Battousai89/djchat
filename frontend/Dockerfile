FROM node:16 AS build-stage

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код Vue.js
COPY . .

# Собираем приложение
RUN npm run build

# Базовый образ для Nginx
FROM nginx:stable-alpine AS production-stage

# Копируем собранные файлы Vue.js из build-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Указываем рабочий порт
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]

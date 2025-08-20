# Используем официальный образ Node.js
FROM node:22-alpine

# Устанавливаем Angular CLI глобально
RUN npm install -g @angular/cli

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости проекта
RUN npm install

# Копируем исходный код приложения
COPY . .

# Открываем порт для приложения
EXPOSE 4200

# Команда для запуска приложения
CMD ["ng", "serve", "--host", "0.0.0.0"]
# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем зависимости для работы с PostgreSQL и сборки пакетов
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта
COPY . .

# Открываем порт для Django
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

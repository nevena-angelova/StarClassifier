# Официален Python образ
FROM python:3.12-slim

# Задаваме работна директория
WORKDIR /app

# Копираме файловете
COPY . /app

# Инсталираме зависимостите
RUN pip install --no-cache-dir -r requirements.txt

# Стартираме приложението
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
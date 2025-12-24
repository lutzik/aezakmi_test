# Agora, задание

## Требования
- Python 3.8+
- Docker

## Установка
1. Склонировать репозиторий
2. Скопировать `.env.example` в `.env` и вставить AGORA_APP_ID и AGORA_APP_CERTIFICATE
3. Создать виртуальное окружение:
	`python3 -m venv venv`
4. Активировать его:
   `source venv/bin/activate`
5. Установить зависимости:
	`pip install -r requirements.txt`
6. Запуск: `PYTHONPATH=src uvicorn main:app --reload`
5. Docker
    `docker-compose up --build`

## Примеры
	http://127.0.0.1:8000/docs

## Тесты
	PYTHONPATH=src python -m pytest

## Затраты времени
	7-8 часов
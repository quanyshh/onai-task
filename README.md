## Тестовое задание
Разработка REST API для обработки запросов с использованием LLM


## Цель проекта
Разработать REST API-сервис, который будет обрабатывать входящие webhook-запросы с помощью LLM и отправлять сгенерированные ответы на указанный endpoint

Сборка Docker контейнера
```bash
docker build -t onai-task
```

Запуск Docker контейнера
```bash
docker run -d -p 8000:8000 onai-task
```
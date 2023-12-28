# recommend-service

## Старт

Для старта проекта необходимо создать файл `.env` в корне проекта.

Перечень переменных виртуального окружения для конфигурации: [.env.example](docker/.env.example).

---
### Для режима DEV

В режиме DEV необходимо указать значение переменной виртуального окружения:
```
ENV=DEV
DEBUG=True
```

При установке `ENV=DEV` для всех ресурсных путей создается префикс: `/dev/`.

Пример запросов для различных сред:

| RESOURCE PATH       | ENV=DEV                   | ENV=PRODUCTION        |
|---------------------|---------------------------|-----------------------|
| admin               | /dev/admin/               | /admin/               |
| GET recommendations | /dev/api/recommendations/ | /api/recommendations/ |

---

Запуск контейнеров:

```shell
docker-compose -f docker/docker-compose.yml up -d
```

Команда для создания суперпользователя (выполняется внутри контейнера `web`):

```shell
python manage.py createsuperuser
```

## Описание API

Для использования API была создана Postman-коллекция, включающая в себя:
- Запросы к API;
- Тесты эндпоинтов.

Файл с коллекцией: [KOZHUKOV.postman_collection.json](KOZHUKOV.postman_collection.json)

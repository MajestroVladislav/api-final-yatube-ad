📌 Проект Yatube API

Это REST API для социальной сети Yatube, реализованное на Django и Django REST Framework.

✏ Описание

API позволяет работать с постами, группами, комментариями и подписками. Используется JWT аутентификация через библиотеку Djoser.

Основные возможности:

⦁ CRUD операции с постами и комментариями
⦁ Просмотр и чтение групп и постов
⦁ Подписка на авторов (модель Follow)
⦁ Авторизация через JWT токены
⦁ Пагинация, поиск подписок по имени автора

✏ Технологии

⦁ Python 3.8+
⦁ Django 3.2+
⦁ Django REST Framework
⦁ Simple JWT
⦁ Djoser

✏ Установка и запуск

1. Клонировать репозиторий:

shell

git clone <адрес вашего репозитория>

2. Создать и активировать виртуальное окружение:

shell

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Установить зависимости:

shell

pip install -r requirements.txt

4. Выполнить миграции:

shell

python manage.py migrate

5. Создать суперпользователя:

shell

python manage.py createsuperuser

6. Запустить сервер разработки:

shell

python manage.py runserver

✏ Использование API

⦁ Все эндпоинты находятся по префиксу: /api/v1/
⦁ Для регистрации и аутентификации используйте эндпоинты Djoser (например, /api/v1/auth/jwt/create/)
⦁ Смотрите документацию Redoc по адресу /redoc/

✏ Тестирование

Для запуска тестов используйте:

pytest

Убедитесь, что виртуальное окружение активировано, и зависимости установлены.
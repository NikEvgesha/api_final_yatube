# Yatube API Project

## Описание
Проект содержит реализацию серверной части Yatube, предоставляющей API для взаимодействия.

Yatube позволяет пользователям публиковать, просматривать и комментировать посты.

## Установка

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:NikEvgesha/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```


```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

5. Запустить проект:

```
python3 manage.py runserver
```

## Примеры API запросов
Полная документация на API доступна после установки по адресу http://127.0.0.1:8000/redoc/

1. Получение публикации по id.
[GET] http://127.0.0.1:8000/api/v1/posts/{id}/

2. Добавление нового комментария к публикации.
[POST] http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

3. Получения списка подписок текущего пользователя.
[GET] http://127.0.0.1:8000/api/v1/follow/

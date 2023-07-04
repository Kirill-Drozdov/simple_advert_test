## SimpleAdvert - тестовое

### О проекте
Данный проект представляет собой сервис для удобного размещения
различных обявлений: `покупка`, `продажа`, `оказание услуг`.


### Технологии
```
python==3.10
alembic==1.7.7
fastapi-users-db-sqlalchemy==4.0.0
fastapi==0.78.0
uvicorn==0.17.6
SQLAlchemy==1.4.36
```
> **Note**:
> Подробный список зависимостей представлен в файле `requirements.txt`.

### Установка

1. Клонировать репозиторий и перейти в него в командной строке:

    ```shell
    git clone git@github.com:Kirill-Drozdov/simple_advert_test.git
    ```

    ```shell
    cd simple_advert_test
    ```

Cоздать и активировать виртуальное окружение с `python 3.10`:

```shell
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла `requirements.txt`:

```shell
python3 -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

Создать файл `.env` и заполнить его по примеру
из файла `.env.template`.


### Запуск

Запустить проект:

```shell
uvicorn app.main:app
```

Запустить проект:

```shell
uvicorn app.main:app
```

### Спецификация

По адресу http://127.0.0.1:8000/docs будет доступна спецификация к проекту,
где представлены примеры запросов к API и структура ответов.

### Об авторе проекта:
Проект выполнил - [Дроздов К.С.](https://github.com/Kirill-Drozdov)

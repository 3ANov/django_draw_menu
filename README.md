## Тестовое задание на позицию Junior Backend Developer
    
Создать виртуальную среду:
``` bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:
```bash
pip install -r requirements.txt
```

Запустить миграции:
``` bash
python manage.py migrate
```
    
Создать суперпользователя, чтоб заходить в админку:
``` bash
python manage.py createsuperuser
```

Загрузить инициализирующие данные:
``` bash
python3 manage.py loaddata ./fixtures/menu.json 
python3 manage.py loaddata ./fixtures/menu_items.json
```

Запустить приложение http://localhost:8000/:
``` bash
python manage.py runserver
```
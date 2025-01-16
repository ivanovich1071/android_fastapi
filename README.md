В папке урока, рядом с папкой fastapi_simble создаем виртуальное окружение

```
python -m venv env
```

у нас получится такая структура:
```
├── android_lesson_2
│   ├── env
│   └── fastapi_simble
```

Переходим в папку fastapi_simble и устанавливаем зависимости в окружение

```
cd fastapi_simble
../env/bin/pip install -r requierments.txt
```

Запускаем uvicorn сервер на порту 5000
```
../env/bin/uvicorn main:app --port 5000
```

Проверяем работу api

```
../env/bin/python
```

```
import requests
import json

url = 'http://127.0.0.1:5000/api/get_answer'
data = {"text": "привет"}

response = requests.post(url, data=json.dumps(data))

print(response.text)
```
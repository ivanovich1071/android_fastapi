import requests
import json

url = 'http://127.0.0.1:5000/api/get_answer'
data = {"text": "Привет"}

try:
    response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    print(f"Статус-код: {response.status_code}")
    print(f"Ответ: {response.json()}")
except requests.exceptions.RequestException as e:
    print(f"Ошибка: {e}")
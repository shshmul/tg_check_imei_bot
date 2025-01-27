import requests
import json
from config import API_TOKEN

url = "https://api.imeicheck.net/api/check-imei"



def validate_imei(imei):
    # Проверка длины IMEI и что ввод цифровой
    return len(imei) == 15 and imei.isdigit()


def get_imei_info(imei):
    # Запрос фзшapi для проверки imei
    response = requests.post('https://imeicheck.net/api/check-imei', data={
        'imei': imei,
        'token': API_TOKEN
    })
    if response.status_code == 200:
        return response.json()
    else:
        return "Ошибка при проверке IMEI"

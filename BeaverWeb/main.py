import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6589467938:AAH9J5TbIUlBnZn7GGorR04Pk2HwqqLx97Y'
offset: int = -2
updates: dict
 

def do_something(message) -> None:
    print(f'Написали {message["text"]}')


while True: 
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something(result['message'])
    time.sleep(3)
    end_time = time.time()
    print(f'Разница end_time и start_time: {end_time - start_time}')
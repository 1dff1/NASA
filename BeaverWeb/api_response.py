import requests


def get_users():
    url = 'https://www.boredapi.com/api/activity/'
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f'Ошибка: {response.status_code}')
        return None
    

def main():
    users = get_users()
    if users:
        print(users["activity"])


if __name__ == '__main__':
    main()
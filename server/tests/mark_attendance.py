import requests
import datetime


def mark_attendance(url, json):
    response = requests.post(url, json=json)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        print('invalid response')
    return {}


url = 'http://127.0.0.1:4000/api_1/mark_attendance'

request_obj = {
    'embedding': [0 for x in range(128)],
    'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

for i in range(100):
    mark_attendance(url, request_obj)

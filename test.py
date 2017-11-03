import requests
import config
from time import sleep
#dict1 = [{'message': {'message_id': '123', 'text': 'rth'}, 'from': {'id': '12', 'name':{'first_name':'fedya','last_name':'pidor'}}}]
#print(type(dict1))
#dict1 = dict(dict1[0])
#print(dict1)
#print(dict1['from']['name']['first_name'])
#print(type(dict1))


def check_last_update_id(data):
    results = data['result']
    total_updates = len(results) - 1
    last_up_id = results[total_updates]
    return last_up_id


def send_request_to_log():
    answer = requests.get(config.url + 'getUpdates')
    return answer.json()


def get_id(info):
    chat_id = info['message']['chat']['id']
    return chat_id


def get_updates(param, request, timeout):
    params = {'offset': param , 'timeout': timeout}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def examine_content():
    boolean_status = None
    last_up = 0
    while boolean_status:
        length = send_request_to_log()['result']
        if len(length) == 0:
            boolean_status = True

        elif len(length) != 0:
            boolean_status = False
            last_up = check_last_update_id(send_request_to_log())['update_id']
    return last_up


def main():
    #up_id = examine_content()

    up_id = check_last_update_id(send_request_to_log())['update_id']
    while True:
        sended = get_updates(up_id, config.url, timeout=20)['result']
        if len(sended) == 0:
            pass
        else:
            print(sended[0])
            up_id += 1
        sleep(0)


if __name__ == '__main__':
     main()
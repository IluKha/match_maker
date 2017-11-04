import requests
import config
from time import sleep


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
    params = {'offset': param, 'timeout': timeout}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def start_examine_content():
    buffer_list = []
    while len(buffer_list) == 0:
        buffer_list = send_request_to_log()['result']
        sleep(config.sleep_time)
    return send_request_to_log()


def type_of_update(mess_from_user, mess):
    if mess_from_user[4] == 'text' and mess['message']['chat']['id'] > 0:
        person_id = mess['message']['from']['id']
        send_mess_toperson(person_id)
    elif mess_from_user[4] == 'new_chat_participant' and mess['message']['new_chat_participant']['id'] == 467092924:
        chat_id = mess['message']['chat']['id']
        send_mess_togroup(chat_id)
    else:
        pass


def send_mess_toperson(person_id ):
    params = {'chat_id': person_id, 'text': 'Привет мне ,короче , нужны твои ФИО , а еще паспортные данные хочу оформить мелкий займ , но ты не бойся ты будешь в плюсе'}
    response = requests.post(config.url + 'sendMessage', data=params)
    return response


def send_mess_togroup(chat_id):
    params = {'chat_id': chat_id, 'text': 'Хей, я бот ,который будет отвечать за праздники и напоминать о них , если ты ,сволочь ,о них забудешь . Добавь меня в личку. with Love @HOOliganJimmybot))'}
    response = requests.post(config.url + 'sendMessage', data=params)
    return response


def main():
    up_id = check_last_update_id(start_examine_content())['update_id']

    while True:
        mess_from_user = get_updates(up_id, config.url, timeout=4)['result']
        if len(mess_from_user) == 0:
            pass
        else:
            mess = mess_from_user[0]
            print(mess_from_user[0])
            mess_from_user = list(mess_from_user[0]['message'])
            type_of_update(mess_from_user, mess)
            print(mess_from_user)
            up_id += 1
        sleep(config.sleep_time)


if __name__ == '__main__':
    main()

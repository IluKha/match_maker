import requests
from time import sleep
import config


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_name(update):
    name = update['message']['from']['first_name']
    return name


def send_mess(chat, name, text):
    params = {'chat_id': chat, 'text': name + text}
    response = requests.post(config.url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(get_updates_json(config.url))['update_id']
    print(update_id,  last_update(get_updates_json(config.url)))
    print(get_name(last_update(get_updates_json(config.url))))
    while True:
        if update_id == last_update(get_updates_json(config.url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(config.url))),
           get_name(last_update(get_updates_json(config.url))), ', you\'re pidor')
           update_id += 1
    sleep(1)


if __name__ == '__main__':  
    main()

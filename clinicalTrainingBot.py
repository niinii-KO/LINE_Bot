#参考：https://qiita.com/UT_ITDaiku/items/48c8c75d35b2005e913d
import requests

line_notify_token = LINE_NOTIFY_TOKEN
line_notify_api = 'https://notify-api.line.me/api/notify'
message = ""

def main(message):
    print('送信メッセージ：' + message)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

if __name__== '__main__':
    main(message)

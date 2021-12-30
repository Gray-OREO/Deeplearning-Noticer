import requests
import time


# You should change 'Eventname' and the personal key 'abcdefghijklmn' by yourselves.
# And you can test it by this programme.
def send_notice(text):
    url = "https://maker.ifttt.com/trigger/" + 'Eventname' + "/with/key/" + 'abcdefghijklmn' + ""
    payload = "{\n    \"value1\": \"" + text + "\"\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)


if __name__ == '__main__':
    a = 1
    b = 2
    now = int(time.time())
    timeArray = time.localtime(now)
    c = time.strftime("%m/%d %H:%M", timeArray)
    DETIAL = "Test！！Learning epoch{}... Current index:{}, Datetime:{}".format(a, b, c)
    send_notice(DETIAL)

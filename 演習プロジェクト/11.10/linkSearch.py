import requests

try :
    url = requests.get(input('urlを入力してください : '))
    url.raise_for_status
    files = open('download.txt', 'wb')
    for chunk in url.iter_content(100000):
        files.write(chunk)
    print('ダウンロード完了')
    files.close()
except Exception as ex:
    print("404 Not Found")

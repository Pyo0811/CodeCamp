import requests
res = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
except Exception as exc:
    print("問題あり: {}".format(exc))

import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(res)
res.raise_for_status()
len(res.text)
print(res.text[:250])

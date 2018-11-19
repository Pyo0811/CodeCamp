from selenium import webdriver
import requests, os, bs4, time

os.makedirs("image", exist_ok=True)

browser = webdriver.Firefox()
browser.get('https://imgur.com/')
search_elem = browser.find_element_by_class_name('Searchbar-textInput')
search_elem.send_keys('Aragaki Yui')
search_elem.submit()
time.sleep(5)

url = browser.current_url

while not url.endswith("#") :
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    pic_elem = soup.select('#pbyDU img')
    if pic_elem == [] :
        print("画像が見つかりませんでした。")
    else :
        pic_url = "http:" + pic_elem[0].get("src")
        print("画像をダウンロード中 {}...".format(pic_url))
        res = requests.get(pic_url)
        res.raise_for_status()

        image_file = open(os.path.join("image", os.path.basename(pic_url)), "wb")

        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

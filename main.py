import requests
from bs4 import BeautifulSoup
import urllib

def get_html(url):
    request = requests.get(url)
    return False if request.status_code == 404 else request.text

def main():

    soup = BeautifulSoup(get_html("https://www.nvidia.com/ru-ru/geforce/graphics-cards/30-series/rtx-3070/"), 'lxml')
    objBuyBtn = soup.find('li', class_="persisting").find('a')
    print(objBuyBtn.text)
    if(objBuyBtn.text.replace('  ', '').replace('\n', '').replace('\t', '').strip().lower() == 'сообщите мне'):
        print("Видеокарта RTX 3070 недоступна для покупки")
        #get_html("https://api.telegram.org/bot1313932292:AAGURlPaN7w3ES08wX6uGMcF9w32p1fopwo/sendMessage?chat_id=1188046499&text=" + urllib.parse.quote("Видеокарта RTX 3070 недоступна для покупки"))
    else:
        #print("Видеокарта RTX 3070 доступна для покупки")
        get_html(
            "https://api.telegram.org/bot1313932292:AAGURlPaN7w3ES08wX6uGMcF9w32p1fopwo/sendMessage?chat_id=1188046499&text=" + urllib.parse.quote(
                "Видеокарта RTX 3070 доступна для покупки"))


if __name__ == '__main__':
    main()

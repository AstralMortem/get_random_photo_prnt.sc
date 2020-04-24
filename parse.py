import random
import requests
import string
import os
from bs4 import BeautifulSoup

headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
main_url = 'https://prnt.sc/'


class Parse():
    def __init__(self):
        super(Parse, self).__init__()
        self.abc = string.ascii_lowercase + '0123456789'
        self.path = os.path.join(os.path.dirname(__file__), 'output/')
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def id_url(self):
        return ''.join([self.abc[random.randint(0, len(self.abc)-1)] for i in range(6)])

    def get_img_path(self):
        url = main_url + self.id_url()
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html)
        img_url = soup.find_all('img')
        return img_url[0]['src']

    def create_path(self):
        return self.path + self.id_url()

    def get_img(self):
        path = self.create_path()
        res = requests.get(self.get_img_path())
        if res.status_code == 200:
            with open(f"{path}.png", 'wb') as f:
                f.write(res.content)


parse = Parse()

if __name__ == '__main__':

    for i in range(100):
        try:
            parse.get_img()
        except:
            continue

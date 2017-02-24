import os
import uuid
import requests
from lxml import html
from selenium import webdriver

class tiraprint:
    def save(self,url):
        filename = '%s.png' % uuid.uuid4().hex

        path = os.path.abspath(os.path.join('data',filename))
        driver = webdriver.PhantomJS()
        driver.set_window_size(1024, 768)
        driver.get(url)
        driver.save_screenshot(path)
        result = self.send(path)
        os.remove(path)
        return result

    def send(self,filename):
        url = 'http://www.freeimagehosting.net/upl.php'
        files = {'file':(filename,open(filename,'rb'),'application/octet-stream')}
        r = requests.post(url, files=files)
        tree = html.fromstring(r.content)
        site_print = tree.xpath('/html/body/center/table[2]/tr/td/img/@src')
        if site_print:
            return site_print[0]
        else:
            return False

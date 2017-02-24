import requests
from lxml import html

class scanurl:
    def consult(self,site):
        response = False
        url = 'http://scanurl.net/'
        headers = {'Host':'scanurl.net','Accept-Language':'en-US,en;q=0.5','Upgrade-Insecure-Requests':'1','Refere':'http://scanurl.net/','Connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0','Accept-Encoding':'gzip, deflate'}
        params = {'u':site,'uesb':'Check This URL'}
        r = requests.get(url,params=params,headers=headers)
        tree = html.fromstring(r.content)
        result = tree.xpath('//*[@class="dtc padding3 border0 bg0 middle right"]/img/@title')
        if result:
            if 'Alert:' in result[0]:
                response = True
        return response

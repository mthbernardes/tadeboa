import requests
from lxml import html

class globalsitesafety:
    def consult(self,url):
        response = dict()
        s = requests.Session()
        r = s.get('https://global.sitesafety.trendmicro.com/index.php')
        cookies = r.cookies
        url = 'https://global.sitesafety.trendmicro.com/result.php'
        data = {'urlname':url,'getinfo':'Check+Now'}
        r = s.post(url,data=data,cookies=cookies)
        tree = html.fromstring(r.content)
        status = tree.xpath('//*[@class="labeltitleresult"]/text()')
        categoria = tree.xpath('//*[@class="labeltitlesmallresult"]/text()')
        if status:
            response['status'] = status[0]
            response['categoria'] = categoria[0]
        else:
            response['status'] = None
            response['categoria'] = None
        return response
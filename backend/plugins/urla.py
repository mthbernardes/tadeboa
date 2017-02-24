import re
import requests
from pprint import pprint
from urllib.parse import urlparse
from plugins.whoyouare import whoyouare
from plugins.globalsitesafety import globalsitesafety
from plugins.exploitation import exploitation
from plugins.tiraprint import tiraprint
from plugins.scanurl import scanurl

class urla:
    def consult(self,url):
        if not (re.match('^https?:\/\/', url)):
            url = 'http://'+url
        try:
            r = requests.head(url,allow_redirects=True)
            url = r.url
        except:
            pass
        parsed = urlparse(url)
        response = dict()
        infos = dict()
        infos['protocol'] = parsed.scheme
        infos['domain'] = parsed.hostname
        infos['parameters'] = parsed.query
        infos['path'] = parsed.path

        #Coleta dados sobre o dominio
        w = whoyouare()
        response['dominio'] = w.consult(infos['domain'])

        #Coleta informacoes de seguranca sobre o dominio
        s = globalsitesafety()
        response['seguranca'] = s.consult(url)

        #Coleta informacoes de seguranca de acordo com o GlobalSiteSafety da TrendMicro
        e = exploitation()
        response['vulnerabilidade'] = e.consult(url)

        #Tira print da pagina
        t = tiraprint()
        response['print'] = t.save(url)

        #Coleta infos no scanurl
        su = scanurl()
        response['scanurl'] = su.consult(url)

        return response

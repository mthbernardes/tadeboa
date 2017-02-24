import re
import whois
import arrow
from pprint import pprint
from requests import get
from dateutil import parser
from pycpfcnpj import cnpj

class whoyouare:
    def consult(self,domain):
        w = whois.whois(domain)
        response = dict()
        if 'domain_name' in w:
            print(w['domain_name'])
            response['dominio'] = w['domain_name'][0] if type(w['domain_name']) is list else w['domain_name']
            created =  w['creation_date'][0] if type(w['creation_date']) is list else w['creation_date']
            response['criado_em_h'] = arrow.get(created).humanize(locale='pt')
            response['criado_em'] = created.strftime('%d/%m/%Y')
            response['registrado_para'] = w['registrar']
            response['dadosEmpresa'] = False
        else:
            response['dominio'] = w['domain']
            created = w['created'][0].split(' ')[0] if type(w['created']) is list else w['created'].split(' ')[0]
            response['criado_em_h'] = arrow.get(parser.parse(created)).humanize(locale='pt')
            response['criado_em'] = parser.parse(created).strftime('%d/%m/%Y')
            response['registrado_para'] = w['owner']
            response['documento_responsavel'] = w['ownerid']
            documento = re.sub(r'[^\w]','',str(w['ownerid']))
            company = self.getCompanyInfos(documento)
            response['dadosEmpresa'] = company
        return response

    def getCompanyInfos(self,document):
        response = None
        if cnpj.validate(document):
            url = 'https://www.receitaws.com.br/v1/cnpj/%s' % document
            r = get(url)
            if b'atividade_principal' in r.content:
                response = r.json()
        else:
            response = False
        return response

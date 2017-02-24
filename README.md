#Instancia ativa
<a href="https://tadeboa-g4mbler.c9users.io/">Ta de boa?</a>
<br>
# Ta de boa?
<pre>
Para identificar se um link que foi enviado por e-mail não é malicioso, é preciso analisar algumas informações, tentar encontrar algum exploração de xss ou csrf na url, identificar pra quem o dominio esta registrado, analisar se ele esta em alguma base de urls maliciosas, o que essa aplicação faz, é simplesmente automatizar todo esse processo,
- Verificação de encurtadores de URL
- Busca de exploração de XSS Reflected e CSRF (Baseado nas regras do PHPIDS)
- Levantamento de informações sobre o dominio
- Busca no <a href= "http://global.sitesafety.trendmicro.com/">Global Sitesafety</a> para identificar se a URL é conhecida pela Trend Micro como maliciosa.
- Busca no <a href= "http://scanurl.net/">ScanURL</a> para identificar se a URL é conhecida pelo Google, PhishTank e WOT como maliciosa.
Ex.:
http://localhost:8080/?url=base64(http://pudim.com.br/)
</pre>

#Instalação
<pre>
cd backend
pip install -r requeriments.txt
sudo apt-get update
sudo apt-get install libxml2-dev libxslt-dev python-dev zlib1g-dev
sudo chmod +x install_phantomjs.sh
sudo ./install_phantomjs.sh
</pre>

#Executando
<pre>
cd backend
gunicorn index:__hug_wsgi__
</pre>

#Interface Web
<pre>
cd frontend
open index.html
</pre>

#TO DO
<pre>
Integração com a API gratuita do Virus Total
<strike>Verificar URL encurtadas</strike>
Verificar arquivos javascripts carregados pela pagina
Melhoria na interface Web (HELP ME)
</pre>

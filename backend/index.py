import hug
import base64
from pprint import pprint
from plugins.urla import urla
from hug_middleware_cors import CORSMiddleware

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.get('/')
def find(url:hug.types.text,output=hug.output_format.json,):
    c = urla()
    url = base64.b64decode(url).decode("utf-8").strip()
    response = c.consult(url)
    return response

@hug.not_found()
def not_found_handler():
    return "Not Found"

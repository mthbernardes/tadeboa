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
    try:
        url = base64.b64decode(url).decode("utf-8").strip()
        response = c.consult(url)
        return response
    except:
        return "ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 5"
@hug.not_found()
def not_found_handler():
    return "Not Found"
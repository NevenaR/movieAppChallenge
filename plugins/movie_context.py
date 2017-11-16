import urllib3
import json

MOVIES_LIST = []

def getMovies():
    headers = {
        'Accept': 'application/json'
    }
    http = urllib3.PoolManager()

    response_body = http.request('GET','https://awa5lhb067.execute-api.eu-central-1.amazonaws.com/dev/movies?category=&title=&star=',headers=headers)
    return json.loads(response_body.data.decode('utf-8'))


def preBuild(site):
    global MOVIES_LIST
    MOVIES_LIST=getMovies()



def preBuildPage(site, page, context, data):
    """
    Add the list of PANORAMAs to every page context so we can
    access them from wherever on the site.
    """
    context['MOVIES_LIST'] = MOVIES_LIST
    return context, data
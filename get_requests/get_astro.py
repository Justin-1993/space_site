import requests
import json

# nasa api key 5aVi5rGAMG5dUXH5KxpmZJWVIdGDjH4f8Os1EEdx

def get_astro_name():
    astro_url = 'http://api.open-notify.org/astros.json'
    astro_req = requests.get(astro_url)
    astro_req = astro_req.content.decode('utf-8')
    astro_req = json.loads(astro_req)
    astros = []
    for people in astro_req['people']:
        astros.append(people['name'])
    return astros

def get_astro_profile(name):
    wiki_url = 'https://en.wikipedia.org/api/rest_v1/page/summary/'

    astro_req = requests.get(f'{wiki_url}{name}')
    astro_req = astro_req.content.decode('utf-8')
    astro_req = json.loads(astro_req)

    return astro_req['extract_html']


def get_iss_now():
    iss_url = 'http://api.open-notify.org/iss-now.json'

    iss_req = requests.get(iss_url)
    iss_req = iss_req.content.decode('utf-8')
    iss_req = json.loads(iss_req)

    lat = iss_req['iss_position']['latitude']
    lon = iss_req['iss_position']['longitude']

    return f'{lon}, {lat}'

def nasa_pic_of_the_day():
    nasa_potd_url = "https://api.nasa.gov/planetary/apod?api_key=5aVi5rGAMG5dUXH5KxpmZJWVIdGDjH4f8Os1EEdx"

    potd_req = potd_req = requests.get(nasa_potd_url)
    potd_req = potd_req.content.decode('utf-8')
    potd_req = json.loads(potd_req)

    potd_url = potd_req['hdurl']

    return potd_url


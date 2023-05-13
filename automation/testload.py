import requests
from time import sleep
from pprint import pprint 
from tqdm import tqdm

url = 'http://139.144.176.188/testload/'
results = {}

for _ in tqdm(range(100)):
    r = requests.get(url)
    name = r.json()['name']
    if name in results:
        results[name] += 1
    else:
        results[name] = 0

pprint(results)
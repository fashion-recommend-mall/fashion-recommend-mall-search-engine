import json
import requests
from tqdm import tqdm

def insert_data_to_elasticsearch(product_list:list):
    putUrl = 'http://localhost:9200/products/_doc/'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    for product in tqdm(product_list):
        r = requests.put(putUrl + product.id, data=json.dumps(product.__dict__,
                         indent=4, sort_keys=True), headers=headers)
        if r.status_code >= 400:
            print("There is an error writing to elasticsearch")
            print(r.status_code)
            print(r.json())
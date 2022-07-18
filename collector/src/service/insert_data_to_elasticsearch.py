"""
This is Insert Data To Elastic Search Module!
"""
import json
import requests
from tqdm import tqdm

def insert_data_to_elasticsearch(product_list:list):
    """
    Title : insert_data_to_elasticsearch

    It insets Product Post to elastic search

    Args :
        - product_list (list<ProductPost>) : [ProductPost() ... ]

    Returns :
        - None
    """
    put_url = 'http://localhost:9200/products/_doc/'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    for product in tqdm(product_list):

        res = requests.put(put_url + product.get_id, data=json.dumps(product.__dict__,
                         indent=4, sort_keys=True), headers=headers)

        if res.status_code >= 400:
            print("There is an error writing to elasticsearch")
            print(res.status_code)
            print(res.json())

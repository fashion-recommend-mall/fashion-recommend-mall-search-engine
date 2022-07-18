"""
This is Create Index Module
"""
import json
import requests

index = {
    "settings": {
      "index": {
          "number_of_shards": 1,
          "number_of_replicas": 1
      },
      "analysis": {
        "analyzer": {
          "nori" : {
            "tokenizer" : "nori_tokenizer"
          }
        }
      }
    },
    "mappings": {
        "properties": {
            "object_id": {
                "type": "text"
            },
            "title": {
                "type": "text"
            },
            "category": {
                "type": "text"
            },
            "image_link": {
                "type": "text"
            },
            "site": {
                "type": "text"
            },
            "price": {
                "type": "integer"
            },
            "reviews": {
                "type": "text",
                "fields": {
                    "analyzed": {
                        "type": "text",
                        "analyzer": "nori"
                    }
                }
            },
            "style": {
                "type": "rank_features"
            }
        }
    }
}

def create_index():
    """
    Title : create_index

    This is pre indexing method!!

    It make products index to search better

    Args :
        - None

    Returns :
        - None
    """
    put_url = 'http://localhost:9200/products'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.put(put_url, data=json.dumps(index,
                         indent=4, sort_keys=True), headers=headers)
    if res.status_code >= 400:
        print("There is an error indexing to elasticsearch")
        print(res.status_code)
        print(res.json())

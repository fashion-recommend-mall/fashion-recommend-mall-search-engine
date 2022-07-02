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
            "id": {
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
    putUrl = 'http://localhost:9200/products'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.put(putUrl, data=json.dumps(index.__dict__,
                         indent=4, sort_keys=True), headers=headers)
    if r.status_code >= 400:
        print("There is an error indexing to elasticsearch")
        print(r.status_code)
        print(r.json())
        

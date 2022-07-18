"""
This is main module
"""
from src.service.create_index import create_index
from src.service.get_data_from_mongodb import get_data_from_mongodb
from src.service.insert_data_to_elasticsearch import insert_data_to_elasticsearch


def main():
    """
    Title :

    This is main method!

    It works below step

    Step : Create Index
    Step : Get Data From Mongodb
    Step : Insert Data To Elasticsearch
    Step : Done
    """
    print("Step : Create Index")
    create_index()
    print("Step : Get Data From Mongodb")
    result_list = get_data_from_mongodb()
    print("Step : Insert Data To Elasticsearch")
    insert_data_to_elasticsearch(result_list)
    print("Step : Done")

"""
This is Get Data From Mongodb Logic Module
"""
from tqdm import tqdm

from src.model.product_post import ProductPost
from src.infra.mongodb_contextmanager import MongodbContextManager


def style_indexing(state:dict):
    """
    Title : style_indexing

    It indexs rank feature with style

    Args :
        - state (dict) : { "frist style" : data1, "seconde style" : data2 }

    Returns :
        - result (dict) : { data1 : 100, data2 : 50 }
    """
    result = {}
    result[state["first style"]] = 100
    result[state["second style"]] = 50
    return result


def price_to_integer(price:str):
    """
    Title : price_to_integer

    It make price to integer

    Args :
        - price (string) : "10,000원"

    Returns :
        - price (integer) : 10000
    """
    delete_won = price.split("원")[0]
    delete_dot = delete_won.replace(",","")
    return int(delete_dot)


def rivews_indexing(reviews:list):
    """
    Title : rivews_indexing

    It make str array to one string

    Args :
        - reviews (list string) : ["a","b","c"]

    Returns :
        - result (str) : abc
    """
    return " ".join(reviews)


def data_to_product(element:dict):
    """
    Title : data_to_product

    It is mapping data to product model

    Args :
        - element (dict) : {"id" : ObjectId() ...}

    Returns :
        - result (ProductPost) : ProductPost{"_id" : _id ...}
    """
    _id = str(element.get("_id"))
    title = element.get("title")
    category = element.get("category")
    image_link = element.get("image_link")
    site = element.get("site")
    price = price_to_integer(element.get("price")) # type: ignore
    reviews = rivews_indexing(element.get("reviews")) # type: ignore
    style = style_indexing(element.get("style")) # type: ignore

    return ProductPost(_id, title, category, image_link, site, price, reviews, style)


def get_data_from_mongodb():
    """
    Title : get_data_from_mongodb

    It get data from mongodb and is mapping Product Post

    Args :
        -

    Returns :
        - product_list (list<ProductPost>)
    """
    with MongodbContextManager() as driver: # type: ignore

        get_data = driver.layer4.find()

        product_list = []

        for element in tqdm(get_data):
            product = data_to_product(element)
            product_list.append(product)

        return product_list

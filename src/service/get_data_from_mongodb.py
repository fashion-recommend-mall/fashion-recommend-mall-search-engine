from tqdm import tqdm

from src.model.ProductPost import ProductPost
from src.infra.mongodb_contextmanager import MongodbContextManager


def style_indexing(state:dict):
    result = {}
    result[state["first style"]] = 100
    result[state["second style"]] = 50
    return result


def price_to_integer(price:str):
    delete_won = price.split("원")[0]
    delete_dot = delete_won.replace(",","")
    return int(delete_dot)


def rivews_indexing(reviews:list):
    return " ".join(reviews)


def data_to_product(element:dict):

    id = str(element.get("_id"))
    title = element.get("title")
    category = element.get("category")
    image_link = element.get("image_link")
    site = element.get("site")
    price = price_to_integer(element.get("price"))
    reviews = rivews_indexing(element.get("reviews"))
    style = style_indexing(element.get("style"))

    return ProductPost(id, title, category, image_link, site, price, reviews, style)


def get_data_from_mongodb():

    with MongodbContextManager() as driver: # type: ignore\

        get_data = driver.layer4.find()

        product_list = []

        for element in tqdm(get_data):
            product = data_to_product(element)
            product_list.append(product)

        return product_list

"""
This is Product Post Module
"""

class ProductPost():
    """
    This is Product Post Model Class

    Attributes:
        id :
        title :
        category :
        image_link :
        site :
        price :
        reviews :
        style :
    """

    def __init__(self, object_id, title, category, image_link, site, price, reviews, style):
        self.object_id = object_id
        self.title = title
        self.category = category
        self.image_link = image_link
        self.site = site
        self.price = price
        self.reviews = reviews
        self.style = style

    @property
    def get_id(self):   #getter
        """
        Id Getter

        returns
          - id (str)
        """
        return self.object_id

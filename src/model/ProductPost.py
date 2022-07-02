class ProductPost(object):
  """
    Represents semantic data for a single product post
  """

  def __init__(self, id, title, category, image_link, site, price, reviews, style):
    self.id = id
    self.title = title
    self.category = category
    self.image_link = image_link
    self.site = site
    self.price = price
    self.reviews = reviews
    self.style = style
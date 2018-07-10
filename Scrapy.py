import scrapy
class StackItem(scrapy.Item):
    name=scrapy.Field()
    pass

from scrapy.item import Item,Field

class StackItem(Item):
    title=Field()
    url = Field()

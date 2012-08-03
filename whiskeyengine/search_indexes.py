from haystack.indexes import *
from haystack import site
from whiskeyengine.models import Whiskey

class WhiskeyIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    distillery = CharField(model_attr='distillery')
    category = CharField(model_attr='category')

site.register(Whiskey, WhiskeyIndex)

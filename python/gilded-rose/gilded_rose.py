""" The Gilded Rose's stock digital twin system """
from item_descriptors import find_descriptor

# pylint: disable=too-few-public-methods

class GildedRose():
    """ Digital twin of GR's item stock """
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """ Age all items using the apropriate descriptor for each one """
        for item in self.items:
            descriptor = find_descriptor(item)
            descriptor.age(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

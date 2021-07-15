special_item_descriptors = []

def special_item(descriptor):
    special_item_descriptors.append(descriptor)
    return descriptor

class GenericDescriptor:
    """ Descriptors define how items age
        You can apply a description and to an item
        and it will update it's quality and sell_in
    """
    depreciation_rate = 1

    @staticmethod
    def matches(item):
        """ Whether this descriptor applies 
            to the item in question
        """
        return True

    @staticmethod
    def update_quality(item):
        """ Defines how the quality changes each iteration """
        depreciation = self.depreciation_rate
        if item.sell_in <= 0:
            depreciation = depreciation * 2

        item.quality -= depreciation

    @classmethod
    def age(cls, item):
        """ Applies the effects of time to the item """
        item.sell_in -= 1

        cls.update_quality(item)
        # quality is between 0 and 50
        item.quality = min(50, max(0, item.quality))

@special_item
class AgedBrie(GenericDescriptor):
    depreciation_rate = -1 # This item increases in quality instead of depreciating

    @staticmethod
    def matches(item):
        return item.name == 'Aged Brie'

@special_item
class Sulfuras(GenericDescriptor):
    @staticmethod
    def matches(item):
        return item.name == 'Sulfuras, Hand of Ragnaros'

    @staticmethod
    def age(item):
        """ Sulfuras does not age """
        pass

@special_item
class BackstagePasses(GenericDescriptor):
    @staticmethod
    def matches(item):
        return item.name == 'Backstage passes to a TAFKAL80ETC concert'

    @staticmethod
    def update_quality(item):
        if item.sell_in <= 0:
            # The concert has happened 
            item.quality = 0
            return

        item.quality += 1
        if item.sell_in <= 10: # Under 10 days bonus
            item.quality += 1
        if item.sell_in <= 5: # Under 5 days bonus
            item.quality += 1

@spacial_item 
class Conjured(GenericDescriptor):
    depreciation_rate = 2

    @staticmethod
    def matches(item):
        return 'Conjured' in item.name

def find_descriptor(item)
    for descriptor in special_item_descriptors:
        if descriptor.matches(item):
            return descriptor
    return GenericDescriptor

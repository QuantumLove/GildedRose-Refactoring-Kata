"""
    Item descriptors describe the behavior of the items.
    This module includes descriptors for all types of items
    sold by the Gilded Rose
"""
special_item_descriptors = []

def special_item(descriptor):
    """ Decorator to register special item descriptors
        in the global list
    """
    special_item_descriptors.append(descriptor)
    return descriptor

class GenericDescriptor:
    """ Descriptors define how items age
        You can apply a description and to an item
        and it will update it's quality and sell_in
    """
    depreciation_rate = 1

    @staticmethod
    def matches(item): # pylint: disable=unused-argument
        """ Whether this descriptor applies
            to the item in question
        """
        return True

    @classmethod
    def update_quality(cls, item):
        """ Defines how the quality changes each iteration """
        depreciation = cls.depreciation_rate
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
    """ Aged brie's descriptor """
    depreciation_rate = -1 # This item increases in quality instead of depreciating

    @staticmethod
    def matches(item):
        return item.name == 'Aged Brie'

@special_item
class Sulfuras(GenericDescriptor):
    """ Sulfuras descriptor """
    @staticmethod
    def matches(item):
        return item.name == 'Sulfuras, Hand of Ragnaros'

    @staticmethod
    def age(item):
        """ Sulfuras does not age """
        item.sell_in -= 1

@special_item
class BackstagePasses(GenericDescriptor):
    """ Descriptor for the category of BackstagePasses items """
    @staticmethod
    def matches(item):
        return 'Backstage passes' in item.name

    @staticmethod
    def update_quality(item):
        if item.sell_in <= 0:
            # The concert has happened
            item.quality = 0
            return

        if item.sell_in <= 5: # Under 5 days bonus
            item.quality += 3
        elif item.sell_in <= 10: # Under 10 days bonus
            item.quality += 2
        else:
            item.quality += 1

@special_item
class Conjured(GenericDescriptor):
    """ Descriptor for the category of Conjured items """
    depreciation_rate = 2

    @staticmethod
    def matches(item):
        return 'Conjured' in item.name

def find_descriptor(item):
    """ Identifies if an item is special and, if so,
        return the descriptor for that item.
        It assumes that an item can only have one special
        description to it.
        If it is not special, the generic descriptor is returned
    """
    for descriptor in special_item_descriptors:
        if descriptor.matches(item):
            return descriptor
    return GenericDescriptor

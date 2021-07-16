""" Tests for special Item descriptor """
import pytest
from gilded_rose import Item
from item_descriptors import Sulfuras

def test_sulfuras_matching():
    """ Test for descriptor matcher """
    item = Item('Sulfuras, Hand of Ragnaros', 43, 80)
    assert Sulfuras.matches(item)

test_data = {
    'test_quality_always_80': (
        Item('Sulfuras, Hand of Ragnaros', 43, 80),
        42,
        80,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_sulfuras_aging(item, end_sell_in, end_quality):
    """ Tests for aging this special item """
    print(item)
    Sulfuras.age(item)
    print(item.sell_in)
    print(item.quality)

    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

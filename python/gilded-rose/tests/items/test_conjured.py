""" Tests for special Item descriptor """
import pytest
from gilded_rose import Item
from item_descriptors import Conjured

def test_conjured_matching():
    """ Test for descriptor matcher """
    item = Item('Conjured Mana Cake', 5, 10)
    assert Conjured.matches(item)

test_data = {
    'test_quality_drops_double': (
        Item('Conjured Foobar', 5, 10),
        4,
        8,
    ),
    'test_quality_drops_double_after_sell_in': (
        Item('Conjured Acai, now with 30% more hp', 0, 10),
        -1,
        6,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_conjured_aging(item, end_sell_in, end_quality):
    """ Tests for aging this special item """
    Conjured.age(item)

    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

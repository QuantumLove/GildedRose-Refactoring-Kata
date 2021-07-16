import pytest
from gilded_rose import Item
from item_descriptors import Conjured

def test_conjured_matching():
    item = Item('Conjured Mana Cake', 10, 5)
    assert Conjured.matches(item)

test_data = {
    'test_quality_drops_double': (
        Item('Conjured Foobar', 10, 5),
        8,
        4,
    ),
    'test_quality_drops_double_after_sell_in': (
        Item('Conjured Acai, now with 30% more hp', 10, 0),
        6,
        -1,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_conjured_aging(item, end_sell_in, end_quality):
    Conjured.age(item)
    
    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

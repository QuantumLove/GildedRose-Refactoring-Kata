""" Tests for special Item descriptor """
import pytest
from gilded_rose import Item
from item_descriptors import AgedBrie

def test_aged_brie_matching():
    """ Test for descriptor matcher """
    item = Item('Aged Brie', 5, 10)
    assert AgedBrie.matches(item)

test_data = {
    'test_quality_increases': (
        Item('Aged Brie', 5, 10),
        4,
        11,
    ),
    'test_quality_increases_double_after_sell_in': (
        Item('Aged Brie', 0, 10),
        -1,
        12,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_aged_brie_aging(item, end_sell_in, end_quality):
    """ Tests for aging this special item """
    AgedBrie.age(item)

    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

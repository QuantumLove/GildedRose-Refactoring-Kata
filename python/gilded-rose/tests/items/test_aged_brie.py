import pytest
from gilded_rose import Item
from item_descriptors import AgedBrie

def test_aged_brie_matching():
    item = Item('Aged Brie', 10, 5)
    assert AgedBrie.matches(item)

test_data = {
    'test_quality_increases': (
        Item('Aged Brie', 10, 5),
        11,
        4,
    ),
    'test_quality_increases_double_after_sell_in': (
        Item('Aged Brie', 10, 0),
        12,
        -1,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_aged_brie_aging(item, end_sell_in, end_quality):
    AgedBrie.age(item)
    
    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

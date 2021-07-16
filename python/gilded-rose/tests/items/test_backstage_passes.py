""" Tests for special Item descriptor """
import pytest
from gilded_rose import Item
from item_descriptors import BackstagePasses

def test_conjured_matching():
    """ Test for descriptor matcher """
    item = Item('Backstage passes to a TAFKAL80ETC concert', 5, 10)
    assert BackstagePasses.matches(item)

test_data = {
    'test_quality_increases': (
        Item('Backstage passes to Live Aid', 40, 10),
        39,
        11,
    ),
    'test_quality_increases_10_days_left': (
        Item('Backstage passes to Live Aid', 11, 10),
        10,
        12,
    ),
    'test_quality_increases_5_days_left': (
        Item('Backstage passes to Live Aid', 6, 10),
        5,
        13,
    ),
    'test_quality_1_days_left': (
        Item('Backstage passes to Live Aid', 2, 10),
        1,
        13,
    ),
    'test_quality_0_days_left': (
        Item('Backstage passes to Live Aid', 1, 10),
        0,
        0,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_conjured_aging(item, end_sell_in, end_quality):
    """ Tests for aging this special item """
    BackstagePasses.age(item)

    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

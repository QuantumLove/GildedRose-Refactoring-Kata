from gilded_rose import Item
from item_descriptors import BackstagePasses

def test_conjured_matching():
    item = Item('Backstage passes to a TAFKAL80ETC concert', 10, 5)
    assert BackstagePasses.matches(item)

test_data = {
    'test_quality_increases': (
        Item('Backstage passes to Live Aid', 10, 40),
        11,
        39,
    ),
    'test_quality_increases_10_days_left': (
        Item('Backstage passes to Live Aid', 10, 11),
        12,
        10,
    ),
    'test_quality_increases_5_days_left': (
        Item('Backstage passes to Live Aid', 10, 6),
        13,
        5,
    ),
    'test_quality_1_days_left': (
        Item('Backstage passes to Live Aid', 10, 2),
        13,
        1,
    ),
    'test_quality_0_days_left': (
        Item('Backstage passes to Live Aid', 10, 1),
        0,
        0,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_conjured_aging(item, end_sell_in, end_quality):
    BackstagePasses.age(item)
    
    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

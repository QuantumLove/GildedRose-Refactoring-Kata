from gilded_rose import Item
from item_descriptors import Sulfuras

def test_sulfuras_matching():
    item = Item('Sulfuras, Hand of Ragnaros', 80, 43)
    assert Sulfuras.matches(item)

test_data = {
    'test_quality_always_80': (
        Item('Sulfuras, Hand of Ragnaros', 80, 43),
        80,
        42,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_sulfuras_aging(item, end_sell_in, end_quality):
    Sulfuras.age(item)
    
    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

from gilded_rose import Item
from item_descriptors import GenericDescriptor

FOO = 'FOO'

def test_item_init():
    name = FOO
    sell_in = 5
    quality = 10
    item = Item(name, sell_in, quality)

    assert item.name = name
    assert item.sell_in = sell_in
    assert item.quality = quality

test_data = {
    'test_quality_drops': (
        Item(FOO, 10, 5),
        9,
        4,
    ),
    'test_quality_drops_last_day': (
        Item(FOO, 10, 2),
        9,
        1,
    ),
    'test_faster_drop_after_sell_in_1': (
        Item(FOO, 10, 1),
        8,
        0,
    ),
    'test_faster_drop_after_sell_in_0': (
        Item(FOO, 10, 0),
        8,
        -1,
    ),
    'test_faster_drop_after_sell_in_-1': (
        Item(FOO, 10, -1),
        8,
        -2,
    ),
    'test_quality_cannot_drop_bellow_0': (
        Item(FOO, 0, -1),
        0,
        -2,
    ),
    'test_quality_capped_at_50': (
        Item(FOO, 100, 10),
        50,
        9,
    ),
}
@pytest.mark.parametrize("item,end_sell_in,end_quality",
                         test_data.values(), ids=test_data.keys())
def test_item_decreases_quality(item, end_sell_in, end_quality):
    GenericDescriptor.age(item)
    
    assert item.sell_in == end_sell_in
    assert item.quality == end_quality

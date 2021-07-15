from gilded_rose import Item, GildedRose
from conftest import FOO

def test_item_init():
    name = FOO
    sell_in = 5
    quality = 10
    item = Item(name, sell_in, quality)

    assert item.name = name
    assert item.sell_in = sell_in
    assert item.quality = quality

TODO add parameterization to account for edge cases
def test_item_decreases_quality(mock_gr):
    start_sell_in = int(mock_gr.items[0].sell_in)
    start_quality = int(mock_gr.items[0].quality)

    mock_gr.update_quality()

    assert mock_gr.items[0].sell_in == start_sell_in - 1
    assert mock_gr.items[0].quality == start_quality - 1

TODO add parameterization to account for edge cases
def test_faster_degrade_after_sell_in_date(mock_gr):
    mock_gr.items[0].sell_in = 0
    start_quality = int(mock_gr.items[0].quality)

    mock_gr.update_quality()

    assert mock_gr.items[0].sell_in == 0
    assert mock_gr.items[0].quality == start_quality - 2

parameterized for different item types
def test_quality_is_capped(item_name, start_quality, start_sell_in)
    TODO after code

    mock_gr.update_quality()

    # Maximum quality is 50
    assert mock_gr.items[0].quality == 50

parameterized for different item types and qualities and sell ins
def test_quality_cant_drop_bellow_0(item_name, start_quality, start_sell_in):
    TODO after code

    mock_gr.update_quality()

    assert mock_gr.items[0].quality == 0
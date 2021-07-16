# -*- coding: utf-8 -*-
from unittest.mock import Mock
from gilded_rose import GildedRose

def test_gilded_rose_init():
    """ The store is properly initialized """
    item = Mock()
    item2 = Mock()

    gilded_rose = GildedRose([item, item2])

    assert len(gilded_rose.items) == 2
    assert gilded_rose.items[0] is item
    assert gilded_rose.items[1] is item2

def test_update_quality(mocker):
    """ Verifies that each item is called 
        with the correct descriptor
    """
    items = range(0,3)
    descriptors = [ Mock(), Mock(), Mock()]

    mock_find_descriptor = mocker.patch('gilded_rose.find_descriptor', side_effect=descriptors)

    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    for item, descriptor in zip(items, descriptors):
        descriptor.age.assert_called_once_with(item)

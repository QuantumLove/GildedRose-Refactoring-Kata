

parameterized for each of the regitered thingies
def test_update_quality(item_details, mock_descriptor):
    """ Verifies that each item is called 
        with the correct descriptor
    """

    TODO -> Upgrade this so it tests with multiple items

    gilded_rose = GildedRose([Item(**item_details)])

    gilded_rose.update_quality()

    mock_descriptor.update_quality.assert_called_once_with(item)


Test case for multiple items in the store?

def test_sanity_check_foo_is_not_special(mock_gr):
    """ All tests assume foo is not a special item
        This test is a failsafe in case that changes
    """
    assert False # TODO

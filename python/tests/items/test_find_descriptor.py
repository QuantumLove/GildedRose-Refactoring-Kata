
import pytest
from item_descriptors import GenericDescriptor, find_descriptor

class MockDescriptor:
    def __init__(self, matching=False):
        self.matching = matching
    def matches(self, item):
        return self.matching

MATCHING_DESCRIPTOR = MockDescriptor(True)

test_data = {
    'test_uses_matching_descriptor': (
        MATCHING_DESCRIPTOR,
        [MockDescriptor(False), MATCHING_DESCRIPTOR],
    ),
    'test_matches_the_first_matching_descriptor': (
        MATCHING_DESCRIPTOR,
        [MATCHING_DESCRIPTOR, MockDescriptor(True)],
    ),
    'test_generic_descriptor_when_no_match': (
        GenericDescriptor,
        [MockDescriptor(False)],
    )
}

@pytest.mark.parametrize("matching_descriptor,special_items",
                         test_data.values(), ids=test_data.keys())
def test_update_quality(matching_descriptor, special_items):
    """ Verifies that each item is paired
        with the correct descriptor
    """
    mocker.patch('item_descriptors.special_item_descriptors', special_items)
    assert matching_descriptor is find_descriptor(Mock())


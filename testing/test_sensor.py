import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_obj():

    mock = Mock()

    mock.request_binary.return_value = '100010'

    return mock

def test_mock_method(mock_obj):

    assert mock_obj.request_binary() == '100010'
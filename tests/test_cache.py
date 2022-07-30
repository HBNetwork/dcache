from dcache import cache


@cache
def slow_function(mock=object):
    mock()
    return True


def test_returns():
    assert slow_function() is True


def test_run_once(mocker):
    mock = mocker.MagicMock()

    assert slow_function(mock) is True
    assert slow_function(mock) is True

    mock.assert_called_once()


def test_run_twice_when_arg_change(mocker):
    mock1 = mocker.MagicMock()
    mock2 = mocker.MagicMock()

    assert slow_function(mock1) is True
    assert slow_function(mock2) is True

    mock1.assert_called_once()
    mock2.assert_called_once()

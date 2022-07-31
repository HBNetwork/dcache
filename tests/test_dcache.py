from unittest.mock import MagicMock

from dcache import Dcache

cache = Dcache()
default_mock = MagicMock()


@cache
def slow_func1(mock=default_mock):
    mock(1)
    return 1


@cache
def slow_func2(mock=default_mock):
    mock(2)
    return 2


def test_returns():
    assert slow_func1() == 1
    assert slow_func2() == 2


def test_run_once(mocker):
    mock = mocker.MagicMock()

    assert slow_func1(mock) == 1
    assert slow_func2(mock) == 2

    assert mock.call_count == 2


def test_run_twice_when_function_change(mocker):
    mock = mocker.MagicMock()

    assert slow_func1(mock) == 1
    assert slow_func2(mock) == 2

    assert mock.call_count == 2
    assert mock.call_args_list == [mocker.call(1), mocker.call(2)]


def test_run_twice_when_arg_change(mocker):
    mock1 = mocker.MagicMock()
    mock2 = mocker.MagicMock()

    assert slow_func1(mock1) == 1
    assert slow_func2(mock2) == 2

    mock1.assert_called_once()
    mock2.assert_called_once()

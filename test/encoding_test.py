import interpreter


def test_encode():
    assert interpreter.encode([]) == [0, 0]
    assert interpreter.encode([1, 0]) == [1, 1, 1, 0, 0, 0]


def test_decode():
    assert interpreter.decode([0, 0]) == []
    assert interpreter.decode([1, 0, 0, 0]) == [0]
    assert interpreter.decode([1, 1, 1, 0, 0, 0]) == [1, 0]


def test_invalid_decode():
    assert interpreter.decode([0, 0, 1, 0]) == []
    try:
        interpreter.decode([1, 1, 0, 1])
    except AssertionError as e:
        assert e

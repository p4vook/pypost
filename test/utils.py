from collections import deque
from typing import List

import pytest

import interpreter


def check_state(cells: List[int], current_pos=0):
    assert interpreter.cells == deque(cells)
    assert interpreter.current_pos == current_pos


@pytest.fixture
def setup_cells():
    interpreter.current_pos = 0
    interpreter.cells = deque([1, 0, 0, 0])
    return list(interpreter.cells)

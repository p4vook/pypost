from test.utils import setup_cells, check_state
from collections import deque
import interpreter


def test_move(setup_cells):
    interpreter.move_right()
    check_state(setup_cells, 1)
    interpreter.move_left()
    check_state(setup_cells, 0)


def test_left_append(setup_cells):
    interpreter.move_left()
    check_state([0] + setup_cells, 0)


def test_right_append(setup_cells):
    interpreter.current_pos = len(setup_cells) - 1
    interpreter.move_right()
    check_state(setup_cells + [0], len(setup_cells))

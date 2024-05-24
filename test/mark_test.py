from test.utils import setup_cells, check_state
import interpreter


def test_mark(setup_cells):
    interpreter.mark()
    setup_cells[0] = 1
    check_state(setup_cells)

    interpreter.mark()
    check_state(setup_cells)


def test_unmark(setup_cells):
    setup_cells[0] = 0
    interpreter.unmark()
    check_state(setup_cells)

    interpreter.unmark()
    check_state(setup_cells)

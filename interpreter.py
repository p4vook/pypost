from collections import deque
from time import sleep
from sys import stdin
import argparse


def encode(s):
    result = []
    for x in s:
        result += [1, 1 if x else 0]
    return result + [0, 0]


def decode(s, start = 0):
    result = []
    i = start
    while True:
        pair = (1 if s[i] else 0, 1 if s[i + 1] else 0)
        assert pair != (0, 1)
        if pair == (0, 0):
            return result
        result.append(pair[1])
        i += 2


def move_left():
    global current_pos
    if current_pos == 0:
        cells.appendleft(0)
    else:
        current_pos -= 1


def move_right():
    global current_pos
    if current_pos == len(cells) - 1:
        cells.append(0)
    current_pos += 1


def mark():
    cells[current_pos] = 1


def unmark():
    cells[current_pos] = 0


def dump():
    print(*cells, sep='')
    print(" " * current_pos + "^")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PTM interpreter")
    parser.add_argument('program', type=argparse.FileType('r'), nargs='*', 
                        help='file with a PTM program to interpret', default=stdin)
    parser.add_argument('--input', type=str, help='input binary string', default='')
    args = parser.parse_args()

    cells = deque(encode([1 if c == "1" else 0 for c in args.input]))
    current_pos = 0
    cnt_ops = 0

    for current_program in args.program:
        with current_program as program_file:
            original_lines = program_file.readlines()
        lines = [line.split("#", 1)[0].split() for line in original_lines]

        current_line = 0
        current_cmd = 0

        while current_line < len(lines):
            prev_line = current_line
    #        print(original_lines[current_line], end='')
            move_occured = False
            while current_cmd < len(lines[current_line]):
                cmd = lines[current_line][current_cmd]
                cnt_ops += 1
                if cmd == "?":
                    assert current_cmd + 2 < len(lines[current_line])
                    arg1 = lines[current_line][current_cmd + 1]
                    arg2 = lines[current_line][current_cmd + 2]
                    move_occured = True
                    current_line = (int(arg1) if cells[current_pos] else int(arg2)) - 1
                    current_cmd = 0
                    break
                if cmd == "1":
                    mark()
                elif cmd == "0":
                    unmark()
                elif cmd == "<":
                    move_left()
                elif cmd == ">":
                    move_right()
                elif cmd == "!":
                    current_line = len(lines)
                    move_occured = True
                    break
                current_cmd += 1

            if lines[prev_line]:
    #            dump()
                pass

            if move_occured:
                continue

            current_line += 1
            current_cmd = 0
    #    print(*decode(cells, current_pos), sep='')


    print(*decode(cells, current_pos), sep='')
    print(f"Finished in {cnt_ops} operations")

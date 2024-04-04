# Post-Turing machine interpreter written in Python

## Syntax

See [ruwiki article on Post-Turing machine](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%B0_%D0%9F%D0%BE%D1%81%D1%82%D0%B0).

A program is a text file with one or more lines.

Lines starting with "#" are automatically skipped.

Hereby $n$, $m$ mean positive integer numbers, denoting the line number of a command.

* If such line doesn't exist, the program finishes. 
* If a line starts with "#", interpreter skips until the first line that does not

There are various commands:

* `V n` -- mark the current cell and go to the $n$-th line of the program
* `X n` -- unmark the current cell and go to the $n$-th line of the program
* `L n` -- move the caret left and go to the $n$-th line of the program
* `R n` -- move the caret right and go to the $n$-th line of the program
* `? n m` -- if there is a mark in current cell, go to $n$-th line of the program, otherwise go to the $m$-th line
* `!` -- end the program immediately

Program can receive an input $S$ -- binary string.

This means that marks to the right of the starting position are set according to the 
bits of $S$, with $0$ encoded to $10$ and $1$ encoded to $11$.
(e. g. input $S = 0101$ will set the marks to $10111011$ with caret positioned at the first $1$).

All the other marks are unset.

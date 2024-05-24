# Post-Turing machine interpreter written in Python

[![Python CI](https://github.com/p4vook/pypost/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/p4vook/pypost/actions/workflows/tests.yml)
[![Tests](https://p4vook.github.io/pypost/badges/tests.svg)](https://p4vook.github.io/pypost/reports/junit/)
[![Coverage](https://p4vook.github.io/pypost/badges/coverage.svg)](https://p4vook.github.io/pypost/reports/coverage/)
[![Flake8](https://p4vook.github.io/pypost/badges/flake8.svg)](https://p4vook.github.io/pypost/reports/flake8/)

## How to use

`python3 interpreter.py <program.ptm> --input <input>`

## Syntax

This syntax tries to be as close as possible to the original Post-Turing machine, while still being programmable.

A program is a text file with one or more lines.

If there is a `#` symbol somewhere in the line, everything after it on that line
(including the symbol itself) will be ignored.

A program is interpreted as a series of commands, commands are whitespace (or newline) separated.

## Command reference

Each command is a symbol `1`, `0`, `<`, `>`, `!` or `?`

There are 5 commands which take no arguments:

* `1` -- mark current cell (if it is already marked, nothing will happen)
* `0` -- erase the mark from current cell (if it isn't marked, nothing will happen)
* `<` -- move caret to the left
* `>` -- move caret to the right
* `!` -- end the program immediately

And there is a command which takes 2 arguments, which must follow
(whitespace or newline separated) immediately after the command itself.

* `? n m` -- if there is a mark in current cell, go to $n$-th line of the program, otherwise go to the $m$-th line

## Control flow

The program starts execution at the first command
(if there are no commands, it exits immediately).

After processing command `!`, program stops execution immediately.

After processing command `1`, `0`, `<` or `>`, the command that follows
immediately after it is processed.

If no such command exists, the program ends execution (equivalent to `!`).

After processing command `? n m`, if there is a mark in current cell,
the first command in the part of a program starting from the $n$-th line is executed. 
Otherwise, the first command in the part of a program starting from the $m$-th line
is executed.

If no such command exists, the program ends execution (equivalent to `!`).

## Encoding convention

Note: we denote a set mark as a `1`, and unset mark as a `0`.

Program can receive an input `S` -- binary string.

This means that marks to the right of the starting position are set according to the 
bits of `S`, with `0` encoded to `10` (**N**) and `1` encoded to `11` (**Y**)
(e.g. input `S = 0101` will set the marks to `10111011` with caret positioned at the first `1`).

All the other marks' values are undetermined.

If a program exited, its output from a program is read in bit pairs from left to right,
starting from the caret position and until receiving a `00` bit pair (`F`).

If a `01` bit pair (**E**) is read, the program is considered failed, and subsequent output will not be read.

Otherwise, the output is decoded back into a binary string with `10` (**N**) decoding to `0` and `11` (**Y**) decoding to `1`.

For example, if after the program exited the values of the marks to the right of the caret
(including the mark under the caret itself) are `1110111100...`, the program's output will be
interpreted as a binary string `1011`.

Another example: an empty program outputs its input.

## Proof of equivalence to original Post-Turing machine

### Computable in this syntax $\implies$ Computable in Post-Turing machine

First of all, let's convert our program to a list of commands.

We can assign a number to each command sequentially, then add an argument to commands
`1`, `0`, `<`, `>`, equal to the sequentially next number after the number of a current command.

`? n m` command can be replaced with `? N M`, where $N$ and $M$ are, respectedly,
numbers of first commands starting from $n$-th line and from $m$-th line.

Afterwards, we can replace commands which "jump" to non-existent command numbers with `!` commands.

This will produce a correct Post-Turing machine program which will be equivalent to the
original program in this syntax, as can be easily seen from the control flow rules.

### Computable in Post-Turing machine $\implies$ Computable in this syntax

First of all, we replace each command number $n$ with a placeholder $p_n$ that refers to the
command that was $n$-th.

Then, we replace each command `1 n`, `0 n`, `< n` or `> n` with the command pairs
(`1`, `? pn pn`), (`0`, `? pn pn`), (`<`, `? pn pn`), (`>`, `? pn pn`).

Afterwards, we put each command on a separate line and replace $p_n$ with the line number
of a command that was originally $n$-th.

This is a correct program in our syntax, which produces equivalent results,
as can be easily seen from the control flow rules.

QED.

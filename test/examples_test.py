import subprocess


def run_example(file: str, input: str) -> bytes:
    res = subprocess.run(["python3", "interpreter.py", f"examples/{file}",
                          "--input", input], capture_output=True)
    return res.stdout


def test_double():
    assert run_example("echo.ptm", "1100").startswith(b"11001100\n")


def test_reverse():
    assert run_example("reverse.ptm", "1101").startswith(b"1011\n")


def test_increment():
    assert run_example("increment.ptm", "1101").startswith(b"0011\n")

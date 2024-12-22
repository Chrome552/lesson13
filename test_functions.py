from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'

def test_hello_who_bax():
    assert hello_who('Bax') == 'Hello, Bax'

def test_hello_who_nax():
    assert hello_who('Nax') == 'Hello, Nax'

def test_hello_who_rax():
    assert hello_who('Rax') == 'Hello, Rax'

def test_salary():
    assert salary(2, 2) != 8
    assert salary(3, 1) != 6
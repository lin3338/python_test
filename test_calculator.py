import pytest
2. from calculator import add, multiply
3.
4. def test_add():
5.     assert add(2, 3) == 5
6.     assert add(-1, 1) == 0
7.
8. def test_multiply():
9.     assert multiply(3, 4) == 12
10.     assert multiply(2, 0) == 0
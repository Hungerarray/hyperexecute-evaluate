import pytest
import time

# 5 test cases with different fixed durations


def test_case_1():
    time.sleep(2)
    assert True


def test_case_2():
    time.sleep(2)
    assert True


def test_case_3():
    time.sleep(2)
    assert True


def test_case_4():
    time.sleep(2)
    assert True


def test_case_5():
    time.sleep(2)
    assert True


def test_case_6():
    time.sleep(2)
    assert True


# 2 test cases that always fail


def test_always_fail_1():
    assert False, "This test always fails."


def test_always_fail_2():
    pytest.fail("This test always fails.")


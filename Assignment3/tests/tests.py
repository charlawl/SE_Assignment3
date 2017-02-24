# from nose.tools import *
# from nose.tools.trivial import eq_, ok_
from SE.Assignment3.light_box import parse_line, switch, on, off
import unittest

class TestSetAdt(unittest.TestCase):
    def test_parse_line_switch(self):
        start, end, fun = parse_line('switch 322,558 through 977,958')
        assert start == (322, 558)
        assert end == (977, 958)


    def test_parse_line_onoff(self):
        start, end, fun = parse_line('turn off 87,577 through 484,608')
        assert start == (87,577)
        assert end == (484,608)

    def test_on(self):
        assert on(True) is True
        assert on(False) is True

    def test_off(self):
        assert off(True) is False
        assert off(False) is False

    def test_switch(self):
        assert switch(True) is False
        assert switch(False) is True

if __name__ == '__main__':
    unittest.main()



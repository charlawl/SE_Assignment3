from light_box import parse_line, switch, on, off, read_uri, LightBox, run_lights
import unittest

class TestLights(unittest.TestCase):

    def setUp(self):
        self.light_box = LightBox(3)
        self.test_buffer = ['3', 'switch 0,1 through 2,2']
        self.test_file = "input_assign3.txt"

    def test_read_file(self):
        read_uri(self.test_file)

    def test_light_change(self):
        new_light = [[True, True, True],[False, False, False],[False, False, False]]
        self.light_box.light_change((0, 0), (0, 2), on)
        self.assertEquals(self.light_box.light, new_light)

    def test_get_coords(self):
        self.assertEquals(self.light_box.get_coords((-4, 7)), (0, 2))
        self.assertEquals(self.light_box.get_coords((1, 2)), (1, 2))

    def test_parse_line_switch(self):
        start, end, fun = parse_line('switch 322,558 through 977,958')
        self.assertEquals(start, (322 , 558))
        self.assertEquals(end, (977 , 958))

    def test_parse_line_onoff(self):
        start, end, fun = parse_line('turn off 87,577 through 484,-608')
        self.assertEquals(start, (87,577))
        self.assertEquals(end, (484,-608))

        start, end, fun = parse_line('turn off 87 ,-577 through 484 , -608')
        self.assertEquals(start, (87, -577))
        self.assertEquals(end, (484, -608))

    def test_on_off_switch(self):
        self.assertTrue(on(True))
        self.assertTrue(on(False))
        self.assertFalse(off(True))
        self.assertFalse(off(False))
        self.assertFalse(switch(True))
        self.assertTrue(switch(False))


    def test_main(self):
        run_lights(self.test_file)

if __name__ == '__main__':
    unittest.main()



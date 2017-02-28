import urllib.request
import re
import argparse
import requests

def read_uri(fname):
    """Opening file or url depending on the prefix of the input. The file is then split on new lines"""
    if fname.startswith('http'):
        r = requests.get(fname)
        return r.iter_lines(decode_unicode=True) # utf decoding only needed for reading from url
    else:
        open_file = open(fname)
        return open_file

class LightBox():
    """Class which handles all lightbox functionality."""
    def __init__(self, size):
        self.light_size = size
        self.light = self.make_lights()


    def make_lights(self):
        """Creates the LED array the size of which depends on the first line of the file."""
        return [[False for _ in range(self.light_size)] for _ in range(self.light_size)]

    def get_coords(self, str_tuple):
        """Checks if co-ordinates are out of range. Negative values are set to zero, values above the max
        are set to the max value"""
        return tuple(min(max(0, int(i)), self.light_size - 1) for i in str_tuple)


    def light_change(self, start, end, instruction):
        """Takes start, end and instruction parameters, and changes light accordingly. Loops through y and then x"""
        start = self.get_coords(start)
        end = self.get_coords(end)
        for j in range(start[1], end[1] + 1):
            for i in range(start[0], end[0] + 1):
                self.light[i][j] = instruction(self.light[i][j])

    def count_lights(self):
        """Sums the number of True (1) on each line of the array and provides the result in lights_on"""
        lights_on = 0
        for line in self.light:
            lights_on += sum(line)
        return lights_on



def parse_line(line):
    """Parsing lines from file. Switch/on/off co-ordinates taken from specific line indices """
    m = re.findall("(-*\d+).*?(-*\d+)", line)
    line = line.split()
    start, end = m

    if len(line[0]) == len('switch'):
        fun = switch
    elif len(line[1]) == len('on'):
        fun = on
    elif len(line[1]) == len('off'):
        fun = off
    else:
        return None
    return start, end, fun


def on(light):
    """Function to handle turning lights on"""
    return True


def off(light):
    """Function to handle turning lights off"""
    return False


def switch(light):
    """Function to handle switching light state"""
    return not light


def main():
    """Main function called"""

    parser = argparse.ArgumentParser(prog='light_box')
    parser.add_argument('-f', nargs='?', help='filename')
    parser.add_argument('-u', nargs='?', help='URL')

    args = parser.parse_args()

    uri = args.f or args.u
    if not uri:
        print("No arguments provided. Please use -h for help.")
        return 1

    test_lights(uri)


def test_lights(uri):

    buffer = read_uri(uri)  # buffer will take arguments from arg parse in the command line
    lightbox = LightBox(size=int(next(buffer)))

    for line in buffer:
        if line:
            result = parse_line(line)
            if result:
                start, end, fun = result
                lightbox.light_change(start, end, fun)

    print(lightbox.count_lights())

import urllib.request
import matplotlib.pyplot as plt
import argparse

#uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
#uri = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt'
#uri = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt'
#uri = 'input_assign3.txt'


def read_uri(fname):
    """Opening file or url depending on the prefix of the input. The file is then split on new lines"""
    if fname.startswith('http'):
        open_file = urllib.request.urlopen(fname)
        return open_file.read().decode('Utf-8').split('\n')
    else:
        open_file = open(fname)
        return open_file.read().split('\n')

#add in .decode('utf-8')

class LightBox():
    """Class which handles all lightbox functionality."""
    def __init__(self, size):
        self.light_size = size
        self.light = self.make_lights()


    def make_lights(self):
        """Creates the LED array the size of which depends on the first line of the file."""
        return [[False for _ in range(self.light_size)] for _ in range(self.light_size)]



def parse_line(line):
    line = line.split()
    if 'switch' in line:
        start = (line[1])
        end = (line[3])
        fun = switch
    elif 'on' in line:
        start = (line[2])
        end = (line[4])
        fun = on
    elif 'off' in line:
        start = (line[2])
        end = (line[4])
        fun = off
    else:
        return None
    return start, end, fun


def on(light):
    return True


def off(light):
    return False


def switch(light):
    return not light


def main():

    buffer = read_uri(uri)
    lightbox = LightBox(size=int(buffer[0]))

    for line in buffer[1::]:
        if line:
            start, end, fun = parse_line(line)
            lightbox.light_change(start, end, fun)
            # Heatmap to show distribution of lights that are on (uncomment for heatmap)
        #plt.pcolor(lightbox.light)
        #plt.show()

    print(lightbox.count_lights())

if __name__ == '__main__':
    main()

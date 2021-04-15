import random
import math

MAX_VAL = 2

report_color_mapper = {
    "-2": "blue",
    "-1": "blue",
    "0": "white",
    "1": "yellow",
    "2": "yellow",
}

colors = {
    "yellow":
    [
        0xcccc00, 0xe6e600, 0xffff00, 0xffff1a, 0xffff33, 0xffff4d
    ],
    "white":
    [
        0xffffff
    ],
    "blue":
    [
        0x0052cc, 0x005ce6, 0x0066ff, 0x1a75ff, 0x3385ff, 0x4d94ff
    ]
}

class Colors:
    def __init__(self, n_leds=1):
        self.n_leds = n_leds

        # Generate a hex color list of self.n_leds size
    def generate_color_list(self, reports):
        colors_dict = self.__get_color_dict(reports)
        color_list = [None] * self.n_leds

        for i in range(self.n_leds):
            keys = list(colors_dict.keys())
            color = keys[random.randint(0, len(keys) - 1)]
            color_list[i] = generate_hex(color)

            colors_dict[color] -= 1
            if colors_dict[color] == 0:
                del colors_dict[color]
        
        return color_list

    # Generate a colors dictionary that sums up to self.n_leds, relative to the reports
    def __get_color_dict(self, reports):
        # Set raw reports dictionary
        report_dict = { }
        for report in reports:
            color = report_color_mapper[str(report)]
            if color not in report_dict.keys():
                report_dict[color] = 0
            report_dict[color] += 1
        
        # Set ceil color
        if "blue" in report_dict.keys():
            ceil_color = "blue"
        else:
            keys = list(report_dict.keys())
            ceil_color = keys[random.randint(0, len(keys) - 1)]

        # Set LEDs colors number dictionary
        n_reports = len(reports)
        colors_dict = { }
        sum = 0
        for color in report_dict.keys():
            n_leds_of_color = self.n_leds * (report_dict[color] / n_reports)
            colors_dict[color] = math.floor(n_leds_of_color)
            sum += colors_dict[color]

            
        while sum != self.n_leds:
            colors_dict[ceil_color] += 1
            sum += 1
        
        return colors_dict

# Generate a hex color out of a string color
def generate_hex(color):
    coloring = random.randint(0, len(colors[color]) - 1)
    return colors[color][coloring]
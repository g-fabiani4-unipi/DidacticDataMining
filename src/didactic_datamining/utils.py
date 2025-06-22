
from collections import defaultdict
import numpy as np


def print_fraction(f, denominator):
    if f.denominator == denominator:
        return f
    else:
        k = denominator/f.denominator
        return '%s/%s' % (f.numerator * k, denominator)


def get_color(distribution):
    ndistr = [1.0 * v / sum(distribution) for v in distribution]
    maxval = max(ndistr)
    argmaxval = np.argmax(ndistr)
    color = '#f7f7f7'
    if maxval <= 0.5:
        color = '#f7f7f7'
    elif 0.5 < maxval <= 0.75:
        color = '#c2a5cf' if argmaxval < len(ndistr) / 2.0 else '#a6dba0'
    elif maxval > 0.75:
        color = '#7b3294' if argmaxval < len(ndistr) / 2.0 else '#008837'

    return color


def default_to_regular(d):
    if isinstance(d, defaultdict):
        d = {k: default_to_regular(v) for k, v in d.items()}
    return d

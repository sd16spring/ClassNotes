"""Exports a dict `states` that maps state codes to lists of polygons.

Author: Oliver Steele <oliver.steele@olin.edu>
License: MIT

Requirements:

    sudo pip install BeautifulSoup
    sudo pip install svg.path
"""

from BeautifulSoup import BeautifulSoup
from collections import OrderedDict
from svg.path import parse_path

states = None
"""A `dict` of state abbreviations (e.g. `"MA"`) to lists of polygons. Each polygon is a list of points.
Each point is a tuple of floats `(x, y)`."""

props = ['start', 'control', 'control1', 'control2', 'end']


def get_segment_control_points(segment):
    """Given an `svg.path` segment, return its list of control points.
    Each control point is a complex number."""

    # segment_type = segment.__class__.__name__
    # assert segment_type in ['Line', 'CubicBezier'], segment_type
    return [getattr(segment, prop) for prop in props if hasattr(segment, prop)]


def path_to_points(path):
    """Given an `svg.path` Path, return its list of control points.
    Each control point is a pair of float `(x, y)`."""

    return [(pt.real, pt.imag)
            for segment in path
            for pt in get_segment_control_points(segment)]


def initialize(svg_filename='Blank_US_Map.svg'):
    """Initialize the `states` global variable."""

    with open(svg_filename, 'r') as svg:
        soup = BeautifulSoup(svg.read(), selfClosingTags=['defs'])
        paths = soup.findAll('path')

    global states
    states = {}
    for p in paths:
        state_name = p.get('id', None)
        path_string = p.get('d', None)
        if not state_name or not path_string:
            continue
        # `svg.path` treats the Move command as though it were Line.
        # Split the path data, in order to collect one Path per contour.
        path_strings = [s for s in path_string.split('m') if s]
        polygons = []
        path_prefix = 'm'
        for path_string in path_strings:
            if path_string[0] not in 'M':
                path_string = path_prefix + path_string
            path = parse_path(path_string)
            polygons.append(path_to_points(path))
            end_pt = path[-1].end
            end_pt = path[0].start
            path_prefix = 'M %f,%f m' % (end_pt.real, end_pt.imag)
        states[state_name] = polygons

    states = OrderedDict(sorted(states.items()))

initialize()

if __name__ == '__main__':
    print states['MA']

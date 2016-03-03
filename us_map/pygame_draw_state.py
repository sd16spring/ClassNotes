"""Sample code for `us_map.py`.

Author: Oliver Steele <oliver.steele@olin.edu>
License: MIT

Requirements:

    sudo pip install BeautifulSoup
    sudo pip install matplotlib
    sudo pip install svg.path
"""

import pygame
import sys
import matplotlib.path
import us_map

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)
LIGHT_GRAY = (191, 191, 191)

STATE = 'CO'

width, height = 640, 480

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)


def point_in_polygon(pt, polygon):
    """Returns True iff `pt` is inside `polygon`.
    `polygon` is a list of tuples `(x, y)`."""

    return matplotlib.path.Path(polygon).contains_point(pt)

# Draw the polygons for the state.
for polygon in us_map.states[STATE]:
    # `polygon` points are tuples `(float, float)`. PyGame requires `(int, int)`.
    points = [(int(x), int(y)) for x, y in polygon]
    # Draw the interior
    pygame.draw.polygon(screen, BLUE, points)
    # Draw the boundary
    pygame.draw.polygon(screen, BLACK, points, 1)

pygame.display.flip()

last_mouse_in_state = False

while True:
    if any(event.type == pygame.QUIT for event in pygame.event.get()):
        sys.exit()

    # Is the mouse inside the state?
    mouse_in_state = any(point_in_polygon(pygame.mouse.get_pos(), polygon) for polygon in us_map.states[STATE])
    # Only print a message if the mouse moved from the inside to the outside, or vice versa
    if mouse_in_state != last_mouse_in_state:
        last_mouse_in_state = mouse_in_state
        if mouse_in_state:
            print 'mouse in state'
        else:
            print 'mouse not in state'

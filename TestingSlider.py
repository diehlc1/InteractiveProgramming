"""Sample code for `us_map.py`.
Author: Oliver Steele <oliver.steele@olin.edu>
License: MIT
Requirements:
    sudo pip install BeautifulSoup
    sudo pip install matplotlib
    sudo pip install svg.path
"""

import pygame
from pygame.locals import *
import sys
import matplotlib.path
import us_map
import os

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 200, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)
LIGHT_GRAY = (191, 191, 191)

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']

STATE = 'TX'

ScreenWidth, ScreenHeight = 1000, 700

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight),1,16)
screen.fill(LIGHT_GRAY)

#windowSurfaceObj = pygame.display.set_mode((ScreenWidth,ScreenHeight),1,16)


#starting position
x = 100
pygame.draw.rect(screen,BLUE,Rect(x,5,10,90))
pygame.display.update(pygame.Rect(0,0,ScreenWidth,ScreenHeight))
print 'before'
s = 0
while s == 0:
    button = pygame.mouse.get_pressed()
    print button
    for i in range(len(button)):
        if button[i] != 0:
            print i
    if button[0] != 0:
        print 'a'
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        a = x - 5
        print a
        if a < 0:
            a = 0
        pygame.draw.rect(screen,LIGHT_GRAY,Rect(0,0,ScreenWidth,ScreenHeight))
        #pygame.display.update(pygame.Rect(0,0,width,height))
        pygame.draw.rect(screen,BLUE,Rect(a,5,10,90))
        pygame.display.update(pygame.Rect(0,0,ScreenWidth,ScreenHeight))
        for event in pygame.event.get():
            if event.type == QUIT:
                s=1
print 'after'

def point_in_polygon(pt, polygon):
    """Returns True iff `pt` is inside `polygon`.
    polygon` is a list of tuples `(x, y)`."""

    return matplotlib.path.Path(polygon).contains_point(pt)

# Draw the polygons for the state.
for polygon in us_map.states[STATE]: #originaly [STATE]
    # `polygon` points are tuples `(float, float)`. PyGame requires `(int, int)`.
    points = [(int(x), int(y)) for x, y in polygon]
    # Draw the interior
    pygame.draw.polygon(screen, BLUE, points)
    # Draw the boundary
    pygame.draw.polygon(screen, BLACK, points, 1)
print 'hi'
pygame.display.flip()

last_mouse_in_state = False

while True:
    if any(event.type == pygame.QUIT for event in pygame.event.get()):
       sys.exit()


# check for ESC key pressed, or pygame window closed, to quit
for event in pygame.event.get():
   if event.type == QUIT:
      pygame.quit()
      sys.exit()
   elif event.type == KEYDOWN:
      if event.key == K_ESCAPE:
         pygame.quit()
         sys.exit()

    # Is the mouse inside the state?
#    mouse_in_state = any(point_in_polygon(pygame.mouse.get_pos(), polygon) for polygon in us_map.states[STATE])
    # Only print a message if the mouse moved from the inside to the outside, or vice versa
#    if mouse_in_state != last_mouse_in_state:
#        last_mouse_in_state = mouse_in_state
#        if mouse_in_state:
#            print 'mouse in state'
#        else:
#            print 'mouse not in state'
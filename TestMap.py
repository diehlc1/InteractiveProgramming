import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEMOTION
import time
from random import choice

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 50, 73)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)
LIGHT_GRAY = (191, 191, 191)

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY']

STATE = 'TX'

class MapView(object):
    """ Visualizes a brick breaker game in a pygame window """
    def __init__(self, model, screen):
        """ Initialize the view with the specified model
            and screen. """
        self.model = model
        self.screen = screen

    def draw(self):
        """ Draw the game state to the screen """
        self.screen.fill(LIGHT_GRAY)

        r = pygame.Rect(self.model.slider.left,
                        self.model.slider.top,
                        self.model.slider.width,
                        self.model.slider.height)
        pygame.draw.rect(self.screen, BLUE, r)
        pygame.display.update()


class Slider(object):
    """ Represents the paddle in our brick breaker game """
    def __init__(self, left, top, width, height):
        """ Initialize the paddle with the specified geometry """
        self.left = left
        self.top = top
        self.width = width
        self.height = height


class MapModel(object):
    """ Stores the game state for our brick breaker game """
    def __init__(self):

        self.slider = Slider(50, 50, 10, 30)

class KeyboardController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for left and right keypresses to
            modify the x position of the paddle """
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.slider.left -= 10
        if event.key == pygame.K_RIGHT:
            self.model.slider.left += 10


class MouseController(object):
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Look for mouse movements and respond appropriately """
        if event.type != MOUSEMOTION:
            return
        self.model.slider.left = event.pos[0]

if __name__ == '__main__':
    pygame.init()
    size = (1000, 700)
    screen = pygame.display.set_mode(size)

    model = MapModel()
    view = MapView(model, screen)
    #controller = KeyboardController(model)
    controller = MouseController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)
        view.draw()
        time.sleep(.001)
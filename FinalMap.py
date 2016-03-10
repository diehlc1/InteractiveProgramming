import os
import pygame, sys
from pygame.locals import *
import us_map
import matplotlib.path

BLACK = (0, 0, 0)
BLUE = (0, 245, 255)

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
STATE = 'TX'

LongState = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Deleware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# set window size
width = 950
height = 650

# initilaise pygame
pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.update(pygame.Rect(0,0,width,height))

class Slider(object):
    """Makes slider"""
    def __init__(self):
        self.sWidth = 8
        self.sHeight = 40
        self.x = width / 2
        self.a = self.x
        pygame.draw.rect(windowSurfaceObj,BLUE,Rect(self.x,600,self.sWidth,self.sHeight))
    def slider_button(self):
        """move slider"""
        button = pygame.mouse.get_pressed()
        if button[0] != 0:
             pos = pygame.mouse.get_pos()
             x = pos[0]
             y = pos[1]
             a = x - self.sWidth
             if a < 0:
                    a = 0
             elif a > width - self.sWidth:
                    a = width - self.sWidth
             pygame.draw.rect(windowSurfaceObj,BLACK,Rect(0,650,width,-60))
             pygame.draw.rect(windowSurfaceObj,BLUE,Rect(a,600,self.sWidth,self.sHeight))
             for i in StateList:
                i.ColorGradient(i.stateDataCompile(a, width))
                i.Draw_Map()
             pygame.display.update(pygame.Rect(0,0,width,height))
             self.a = a

slider = Slider()
a = slider.a

class State(object):
    """Makes and draws a state"""
    def __init__(self, state, color, csvname):
        self.state = state
        self.color = color
        self.csvname = csvname

    def stateDataCompile(self, sliderposition, screenMax):

        stateData = open(self.csvname, 'r')
        readAll = stateData.read()

        row_list = readAll.split('\n')
        del row_list[len(row_list)-1], row_list[len(row_list)-1]

        ozone = []
        date = []

        for row in row_list:
            data_point = row.split(',')
            # if row == row_list[0]:
            #     statename = data_point[14]
            ozone.append(data_point[3])
            date.append(data_point[0])

        ozone_sum = float(ozone[0])
        sums_list = []
        # list_of_dates = [date[0]]
        for day in range(1,len(date)-1):
            if date[day] != date[day-1]:
                sums_list.append(ozone_sum)
                ozone_sum = float(ozone[day])
                # list_of_dates.append(date[day])
            else:
                ozone_sum += float(ozone[day])

        percentTotal = float(sliderposition) / float(screenMax)
        datePos = int(percentTotal * (len(sums_list)-1))
        data4date = sums_list[datePos]
        # the_date = list_of_dates[datePos]
        stateData.close()

        return data4date

    def point_in_polygon(self, pt, polygon):
        """Returns True iff `pt` is inside `polygon`.
        polygon` is a list of tuples `(x, y)`."""

        return matplotlib.path.Path(polygon).contains_point(pt)

    def ColorGradient(self, a):
        """Determines shade of blue/black"""
        percentBlue = a/10. #((float(a)-width)/(-width))
        self.color = (0, 245*percentBlue, 255*percentBlue)
        
    def Draw_Map(self):
        """draws state on screen, color determined by ColorGradient()"""
        for polygon in us_map.states[self.state]: #originaly [STATE]
            # `polygon` points are tuples `(float, float)`. PyGame requires `(int, int)`.
            points = [(int(x), int(y)) for x, y in polygon]
            # Draw the interior
            pygame.draw.polygon(windowSurfaceObj, self.color, points)
            # Draw the boundary
            pygame.draw.polygon(windowSurfaceObj, BLACK, points, 1)
        pygame.display.flip()

StateList = []
for i in range(len(STATES)):
    csvName = 'ad_viz_plotval_data(%s).csv' % i
    StateList.append(State(STATES[i], (0, 245/2., 255/2.), csvName))
    StateList[-1].Draw_Map()


s = 0
while s == 0:
    slider.slider_button()

# check for ESC key pressed, or pygame window closed, to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                 pygame.quit()
                 sys.exit()
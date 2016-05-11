''' Several classes for simplified drawing '''
from __future__ import division
import pygame as pg

class Point(object):
    ''' 2D point '''
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = int(x)
        self.y = int(y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __div__(self, k):
        return Point(self.x / k, self.y / k)

    def __call__(self):
        return (self.x, self.y)
        
    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)

class ScreenTrans(object):
    ''' Screen transformation '''
    def __init__(self, piv_x, piv_y):
        ''' piv_x, piv_y: Coordinates of the point (in the screen reference) to
        be considered the origin '''
        super(ScreenTrans, self).__init__()
        self.piv_x = piv_x
        self.piv_y = piv_y

    def trans(self, p):
        ''' ScreenPoint to point '''
        return Point(p.x - self.piv_x, self.piv_y + p.y)

    def itrans(self, p):
        ''' Point to ScreenPoint '''
        return Point(p.x + self.piv_x, self.piv_y - p.y)

class Draw(object):
    ''' Draw on screen using an arbitrary frame of reference '''
    def __init__(self, screen, piv_x, piv_y):
        ''' piv_x, piv_y: Coordinates of the point (in the screen reference) to
        be considered the origin '''
        super(Draw, self).__init__()
        self.screen = screen
        self.T = ScreenTrans(piv_x, piv_y)

    def draw_line(self, color, p1, p2):
        ''' Draw a line segment from p1 to p2, given color '''
        _p1 = self.T.itrans(p1)
        _p2 = self.T.itrans(p2)
        pg.draw.line(self.screen, color, _p1(), _p2())

    def draw_circle(self, color, center, radius, width=1):
        ''' Draw a circle given center, radius and color '''
        _c = self.T.itrans(center)
        pg.draw.circle(self.screen, color, _c(), radius, width)

def main():
    ''' Run a test '''
    pg.init()
    width = height = 200
    screen = pg.display.set_mode((width, height))
    draw = Draw(screen, width / 2, height / 2)

    p1 = Point(0, 50)
    p2 = Point(50, 0)
    draw.draw_line((255,255,255), p1, p2)
    draw.draw_circle((255,255,255), p1 + p2, 5)

    end = False
    while not end:
        for event in pg.event.get():
    		if event.type == pg.QUIT:
    			end = True
        pg.display.update()

if __name__ == '__main__':
    main()

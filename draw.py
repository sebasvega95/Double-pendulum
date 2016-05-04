from __future__ import division
import pygame as pg

class Point(object):
    ''' 2D pioint '''
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

class ScreenTrans(object):
    """ Screen transformation """
    def __init__(self, w, h):
        super(ScreenTrans, self).__init__()
        self.width = w
        self.height = h

    def trans(self, p):
        ''' ScreenPoint to point '''
        return Point(p.x - self.width / 2, self.height / 2 + p.y)

    def itrans(self, p):
        ''' Point to ScreenPoint '''
        return Point(p.x + self.width / 2, self.height / 2 - p.y)

class Draw(object):
    def __init__(self, screen, w, h):
        super(Draw, self).__init__()
        self.width = w
        self.height = h
        self.screen = screen
        self.T = ScreenTrans(w, h)

    def draw_line(self, color, p1, p2):
        _p1 = self.T.itrans(p1)
        _p2 = self.T.itrans(p2)
        pg.draw.line(self.screen, color, _p1(), _p2())

    def draw_circle(self, color, center, radius, width=1):
        _c = self.T.itrans(center)
        pg.draw.circle(self.screen, color, _c(), radius, width)

def main():
    pg.init()
    width = height = 200
    screen = pg.display.set_mode((width, height))
    draw = Draw(screen, width, height)

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

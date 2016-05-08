''' Draw the double pendulum '''
from __future__ import division
from draw import Point, Draw
from calc import DoublePendulum
import pygame as pg 
import math

fps = 60

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
grey = (84, 84, 84)

width = 800
height = 600

def main():
    theta1 = 90 # float(input('Theta1 (degrees): '))
    theta2 = 180 # float(input('Theta2 (degrees): '))
    speed1 = 5 # float(input('Vel theta1 (rad/s): '))
    speed2 = 3 # float(input('Vel theta2 (rad/s): '))
    
    theta1 *= math.pi / 180
    theta2 *= math.pi / 180
    m = 1 # float(input('Mass (kg): '))
    l = 1 # float(input('Lenght (m): '))
    
    pendulums = DoublePendulum(1 / fps, theta1, theta2, speed1, speed2, l, m)
    scale = height / 4
    screen = pg.display.set_mode((width, height))
    canvas = Draw(screen, width / 2, height / 3)
    piv = Point(0, 0)
    
    pg.init()
    clk = pg.time.Clock()
    end = False
    path = []
    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True
        screen.fill(white)
        
        theta1, theta2 = pendulums.solve()
        p1 = Point(math.sin(theta1) * scale, -math.cos(theta1) * scale)
        p2 = p1 + Point(math.sin(theta2) * scale, -math.cos(theta2) * scale)
        # print piv, p1, p2
        path.append(p2)
        canvas.draw_line(black, piv, p1)
        canvas.draw_line(black, p1, p2)
        canvas.draw_circle(red, p1, 3, 0)
        canvas.draw_circle(red, p2, 3, 0)
        canvas.draw_circle(blue, piv, 3)
        
        if len(path) > 1:
            for i in xrange(1, len(path)):
                canvas.draw_line(dark_blue, path[i], path[i - 1])
        
        pg.display.update()
        clk.tick(fps)

if __name__ == '__main__':
    main()
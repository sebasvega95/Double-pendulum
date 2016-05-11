''' Calculate the double pendulum angles and speeds '''
from __future__ import division
from math import sin, cos

g = 9.8

class Integrator(object):
    ''' Integrator for solving differential equations '''
    def __init__(self, _sum, dx):
        ''' _sum is the initial value of the target function and dx is the step
        of the independent variable '''
        super(Integrator, self).__init__()
        self.sum = _sum
        self.dx = dx

    def __call__(self, f):
        ''' Get the area under the curve of f and accumulate for the 
        next call '''
        self.sum += self.dx * f
        return self.sum

class DoublePendulum(object):
    ''' Numerical simulation of a double pendulum system using the angles of
    the pendulums '''
    def __init__(self, dt, th10=0, th20=0, thp10=0, thp20=0, l=1, m=1):
        ''' dt is the time-step, th10 and th20 are the initial angles, thp10 and
        thp20 are initial speeds, l is the length of the pendulums and m their 
        mass '''
        super(DoublePendulum, self).__init__()
        self.theta1 = th10
        self.theta2 = th20
        self.speed1 = thp10
        self.speed2 = thp20
        self.m = m
        self.l = l

        self.int_s1 = Integrator(thp10, dt)
        self.int_s2 = Integrator(thp20, dt)
        self.int_t1 = Integrator(th10, dt)
        self.int_t2 = Integrator(th20, dt)

    def f1(self, t1, t2, s1, s2):
        ''' Acceleration 1 in terms of the system variables '''
        num = -3 * g * sin(t1) - g * sin(t1 - 2 * t2) \
              - 2 * self.l * sin(t1 - t2) * (s2**2 + s1**2 * cos(t1 - t2))
        den = self.l * (3.0 - cos(2 * t1 - 2 * t2))
        return num / den

    def f2(self, t1, t2, s1, s2):
        ''' Acceleration 2 in terms of the system variables '''
        num = 2 * sin(t1 - t2) * (self.l * s1**2 + 2 * g * cos(t1) + \
              s2**2 * cos(t1 - t2))
        den = self.l * (3.0 - cos(2 * t1 - 2 * t2))
        return num / den

    def solve(self):
        ''' Numerically solve the system angles for a single time step '''
        accel1 = self.f1(self.theta1, self.theta2, self.speed1, self.speed2)
        accel2 = self.f2(self.theta1, self.theta2, self.speed1, self.speed2)
        self.speed1 = self.int_s1(accel1)
        self.speed2 = self.int_s2(accel2)
        self.theta1 = self.int_t1(self.speed1)
        self.theta2 = self.int_t2(self.speed2)

        return (self.theta1, self.theta2)

def main():
    ''' Run the program '''
    import matplotlib.pyplot as plt
    import numpy as np
    dt = 0.01
    t = np.arange(0, 10, dt)
    pendulums = DoublePendulum(dt, 1.4, 2.5)

    theta1, theta2 = [], []
    print 'Simulating...'
    for ti in t:
        _thetas = pendulums.solve()
        theta1.append(_thetas[0])
        theta2.append(_thetas[1])
    theta1 = np.array(theta1)
    theta2 = np.array(theta2)
    print 'Done!'

    plt.subplot(2, 1, 1)
    plt.plot(t, theta1)
    plt.subplot(2, 1, 2)
    plt.plot(t, theta2)
    plt.show()

if __name__ == '__main__':
    main()

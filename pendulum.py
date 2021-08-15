from typing import Tuple
from math import sin, cos, pi, pow
import pygame

class Pendulum:
    
    def __init__(self) -> None:
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.angular_acceleration1 = 0
        self.angular_acceleration2 = 0
        self.angular_velocity1 = 0
        self.angular_velocity2 = 0
        self.length1 = 230
        self.length2 = 170
        self.mass1 = 10
        self.mass2 = 10
        self.angle1 = 3*pi/4 - 0.15
        self.angle2 = 3*pi/4
        self.set_cartesian_coordinates()
        self.gravity = 0.5
        self.radius = 10

    def set_cartesian_coordinates(self) -> None:
        self.x1 = int(self.length1*sin(self.angle1))
        self.y1 = int(self.length1*cos(self.angle1))
        self.x2 = int(self.x1 + (self.length2*sin(self.angle2)))
        self.y2 = int(self.y1 + (self.length2*cos(self.angle2)))
        
    def update(self) -> None:
        self.update_first_mass()
        self.update_second_mass()
        self.angular_velocity1 += self.angular_acceleration1
        self.angular_velocity2 += self.angular_acceleration2
        self.angle1 += self.angular_velocity1
        self.angle2 += self.angular_velocity2
        self.set_cartesian_coordinates()

    def update_first_mass(self) -> None:
        self.angular_acceleration1 = (-self.gravity * (2 * self.mass1 + self.mass2) * sin(self.angle1) - self.mass2 * self.gravity * sin(self.angle1 - 2 * self.angle2) - 2 * sin(self.angle1 - self.angle2) * self.mass2 * ((pow(self.angular_velocity2, 2) * self.length2 + pow(self.angular_velocity1, 2) * self.length1*cos(self.angle1 - self.angle2))))/(self.length1*(2 * self.mass1 + self.mass2 - self.mass2 * cos(2 * self.angle1 - 2 * self.angle2)))

    def update_second_mass(self) -> None:
        self.angular_acceleration2 = (2 * sin(self.angle1 - self.angle2) * (pow(self.angular_velocity1, 2) * self.length1*(self.mass1 + self.mass2) + self.gravity * (self.mass1 + self.mass2) * cos(self.angle1) + pow(self.angular_velocity2, 2) * self.length2 * self.mass2 * cos(self.angle1 - self.angle2)))/(self.length2*(2*self.mass1 + self.mass2 - self.mass2 * cos(2*self.angle1-2*self.angle2)))

    def render(self, screen, offset: Tuple[int, int]) -> None:
        # pendulum base
        x1 = self.x1 + offset[0]
        x2 = self.x2 + offset[0]
        y1 = self.y1 + offset[1]
        y2 = self.y2 + offset[1]
        pygame.draw.circle(surface = screen, color = (255, 255, 255), center = (offset[0], offset[1]), radius = self.radius)
        pygame.draw.circle(surface = screen, color = (255, 255, 255), center = (x1, y1), radius = self.radius)
        pygame.draw.line(surface = screen, color = (255, 255, 255), start_pos = (offset[0], offset[1]), end_pos = (x1, y1), width = 2)
        pygame.draw.circle(surface = screen, color = (255, 255, 255), center = (x2, y2), radius = self.radius)
        pygame.draw.line(surface = screen, color = (255, 255, 255), start_pos = (x1, y1), end_pos = (x2, y2), width = 2)

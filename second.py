from utils import map_range
import pygame
import utils
import math
from color import Color

class Second:

    def __init__(self, second, screen, font):
        self.screen = screen
        self.font = font
        self.second = second
        self.rad_second = utils.map_range(self.second, 0, 60, 0, 2 * math.pi)
    
    def draw_text(self, center, radius_text_second):
        text_seconds = self.font.render(f"{self.second}", False, Color.white)
        text_second_position = utils.circle_point(center, radius_text_second, self.rad_second)
        self.screen.blit(text_seconds, text_second_position)
    
    def draw_pointer(self, center, radius_pointer_second):
        pointer_second_position = utils.circle_point(center, radius_pointer_second, self.rad_second)
        pygame.draw.line(self.screen, Color.white, center, pointer_second_position)
    
    def draw_arc(self, center, radius_second):
        start_point_seconds = (center[0] - radius_second, center[1] - radius_second)
        pygame.draw.arc(self.screen, Color.white, pygame.Rect(*start_point_seconds, 2 * radius_second, 2 * radius_second), -self.rad_second + math.pi / 2, math.pi / 2, width=4)


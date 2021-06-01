import utils
import math
import pygame
from color import Color

class Minute:

    def __init__(self, minute, screen, font):
        self.screen = screen
        self.font = font
        self.minute = minute
        self.rad_minute = utils.map_range(self.minute, 0, 60, 0, 2 * math.pi)
    
    def draw_text(self, center, radius_text_minute):
        text_minutes = self.font.render(f"{self.minute}", False, Color.white)
        text_minute_position = utils.circle_point(center, radius_text_minute, self.rad_minute)
        self.screen.blit(text_minutes, text_minute_position)
    
    def draw_pointer(self, center, radius_pointer_minute):
        pointer_minute_position = utils.circle_point(center, radius_pointer_minute, self.rad_minute)
        pygame.draw.line(self.screen, Color.pink, center, pointer_minute_position)
    
    def draw_arc(self, center, radius_minute):
        start_point_minutes = (center[0] - radius_minute, center[1] - radius_minute)
        pygame.draw.arc(self.screen, Color.pink, pygame.Rect(*start_point_minutes, 2 * radius_minute, 2 * radius_minute), -self.rad_minute + math.pi / 2, math.pi / 2, width=4)
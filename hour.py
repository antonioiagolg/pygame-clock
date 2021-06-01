import utils
import math
import pygame

from color import Color

class Hour:

    def __init__(self, hour, screen, font):
        self.hour = hour
        self.screen = screen
        self.font = font
        self.rad_hour = utils.map_range(self.hour % 12, 0, 12, 0, 2 * math.pi)
    
    def draw_text(self, center, radius_text_hour):
        text_hours = self.font.render(f"{self.hour % 12}", False, Color.white)
        text_hour_position = utils.circle_point(center, radius_text_hour, self.rad_hour)
        self.screen.blit(text_hours, text_hour_position)
    
    def draw_pointer(self, center, radius_pointer_hour):
        pointer_hour_position = utils.circle_point(center, radius_pointer_hour, self.rad_hour)
        pygame.draw.line(self.screen, Color.dark_pink, center, pointer_hour_position)
    
    def draw_arc(self, center, radius_hour):
        start_point_hours = (center[0] - radius_hour, center[1] - radius_hour)
        pygame.draw.arc(self.screen, Color.dark_pink, pygame.Rect(*start_point_hours, 2 * radius_hour, 2 * radius_hour), -self.rad_hour + math.pi / 2, math.pi / 2, width=4)
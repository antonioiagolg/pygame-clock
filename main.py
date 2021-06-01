import pygame
from datetime import datetime

from second import Second
from minute import Minute
from hour import Hour

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MF', 30)

done = False

while not done:
    now = datetime.now()
    seconds = now.second
    minutes = now.minute
    hours = now.hour

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill((0, 0, 0))
    second_pencil = Second(seconds, screen, font)
    second_pencil.draw_text(screen.get_rect().center, 230)
    second_pencil.draw_pointer(screen.get_rect().center, 60)
    second_pencil.draw_arc(screen.get_rect().center, 200)

    minute_pencil = Minute(minutes, screen, font)
    minute_pencil.draw_text(screen.get_rect().center, 170)
    minute_pencil.draw_pointer(screen.get_rect().center, 50)
    minute_pencil.draw_arc(screen.get_rect().center, 150)

    hour_pencil = Hour(hours, screen, font)
    hour_pencil.draw_text(screen.get_rect().center, 130)
    hour_pencil.draw_pointer(screen.get_rect().center, 20)
    hour_pencil.draw_arc(screen.get_rect().center, 100)

    pygame.display.flip()
    clock.tick(60)
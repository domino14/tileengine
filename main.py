#!/usr/bin/python

import pygame
from tile_engine import TileEngine

viewport_dims = (900, 600)

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode(viewport_dims)
    pygame.display.set_caption('Tile Engine')
    pygame.key.set_repeat(500, 30)
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    engine = TileEngine(viewport_dims)
    engine.blit_map(background)
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    x_tl = 0
    y_tl = 0
    step_size = 3
    # Event loop
    while 1:
        re_render = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_LEFT:
                    re_render = True
                    x_tl -= step_size
                    if x_tl < 0:
                        x_tl = 0
                if event.key == pygame.K_RIGHT:
                    re_render = True
                    x_tl += step_size
                if event.key == pygame.K_UP:
                    re_render = True
                    y_tl -= step_size
                    if y_tl < 0:
                        y_tl = 0
                if event.key == pygame.K_DOWN:
                    re_render = True
                    y_tl += step_size

        if re_render:
            engine.set_viewport_topleft((x_tl, y_tl))
            engine.blit_map(background)
            screen.blit(background, (0, 0))
            pygame.display.flip()


if __name__ == '__main__': main()

import pygame, controus
from gun import Gun
from  pygame.sprite import Group
from im import  Im

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('dsa')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    im = Im(screen)

    while True:
        controus.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controus.update(bg_color, screen, gun, im, bullets)
        controus.update_bullets(bullets)

run()
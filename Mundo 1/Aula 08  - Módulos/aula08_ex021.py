# Tocando mp3

import pygame

pygame.init()
pygame.mixer.music.load('alone_color_out.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
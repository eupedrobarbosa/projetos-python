import pygame

#Reproduzindo uma música com importações

pygame.init()
pygame.mixer.music.load('scripts-python\exercicios\kerosene.mp3')
pygame.mixer.music.play
input()
pygame.event.wait()


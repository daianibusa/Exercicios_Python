#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('exercicio021.mp3')#chama o arquivo da música
pygame.mixer.music.play()#starta o arquivo
pygame.event.wait()#espera finalizar o arquivo para encerrar o rpograma


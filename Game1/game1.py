import pygame
from pygame import gfxdraw
import random

pygame.init()
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

bg_color = pygame.Color("#001219")
prop_color = pygame.Color("#fefae0")

ball_radius = 15
player_width, player_height = 10, 150

ball = pygame.Rect(screen_width//2-ball_radius, screen_height//2-ball_radius, ball_radius*2, ball_radius*2)
player1 = pygame.Rect(0, screen_height//2-player_height//2, player_width, player_height)
player2 = pygame.Rect(screen_width-player_width, screen_height//2-player_height//2, player_width, player_height)

ball_speed_x, ball_speed_y = 5, 5
player_speed = 5
player1_delta, player2_delta = 0, 0
player1_score, player2_score = 0, 0

clock = pygame.time.Clock()
font = pygame.font.SysFont("inkfree", 35)


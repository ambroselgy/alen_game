import pygame
import sys
from settings import Settings

def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(str(event.key)+"按下")

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Keyboard by Diya")

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        check_events()

run_game()
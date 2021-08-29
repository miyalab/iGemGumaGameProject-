'''
Project Name : iGemGunmaGameProject
File Name    : rpg_main.py
Description  : メインファイル
'''

#----------------------------
# import
#----------------------------
import os
import sys
import pygame
import pygame.locals
import random

openingImg = pygame.image.load("img/opening.png")

#----------------------------
# main program
#----------------------------
def main():
    # debug mode select
    DEBUG_MODE: int = 0
    
    # pygame init
    pygame.init()

    # game system import
    import rpg_define as idef
    import rpg_battle as ibattle
    import rpg_map as imap
    import rpg_staffroll as istaff

    # window init
    pygame.display.set_caption(idef.WINDOW_NAME);
    screen = pygame.display.set_mode(idef.WINDOW_SIZE)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,80)
    tmr: int = 0
    
    if DEBUG_MODE == 1:
        print("debug battle")
        user = idef.player()
        user.Name = "大腸菌"
        user.Command.append("プラスミド1")
        user.Command.append("プラスミド2")
        user.Command.append("プラスミド3")
        ibattle.BattleMain(screen, clock, user, 5)
        
    elif DEBUG_MODE == 2:
        print('debug map')
        imap.MapMain(screen, clock)

    elif DEBUG_MODE == 3:
        print("staff roll check")
        istaff.StaffrollMain(screen, clock)

    while True:
        key = 0

        # event process
        for event in pygame.event.get():
            # program exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # key down event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.locals.K_UP:
                    key = key | idef.KEY_UP
                elif event.key == pygame.locals.K_DOWN:
                    key = key | idef.KEY_DOWN
                elif event.key == pygame.locals.K_LEFT:
                    key = key | idef.KEY_LEFT
                elif event.key == pygame.locals.K_RIGHT:
                    key = key | idef.KEY_RIGHT
                
                if event.key == pygame.locals.K_SPACE:
                    key = key | idef.KEY_SELECT

                if event.key == pygame.locals.K_KP_ENTER or event.key == pygame.locals.K_RETURN:
                    key = key | idef.KEY_ENTER

                # 連射後のご入力防止
                pygame.event.clear()

        # enter key 入力まち
        if key & idef.KEY_ENTER == idef.KEY_ENTER:
             imap.MapMain(screen, clock)
        
        screen.blit(openingImg, [0,0])

        pygame.display.update()
        clock.tick(33)
                


# メインプログラム実行
if __name__  == '__main__':
    main()

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------
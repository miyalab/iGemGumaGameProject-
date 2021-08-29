'''
Project Name : iGemGunmaGameProject
File Name    : rpg_staffroll.py
Description  : スタッフロールファイル
'''

#----------------------------
# import
#----------------------------
import rpg_define as idef
import const
import pygame
import pygame.locals
import sys
import random

#----------------------------
# constant value
#----------------------------
ROLL_FONT_SIZE: int = 20

#--------------------------------------------------
# battle main function
#--------------------------------------------------
def StaffrollMain(bg, clk):
    # font set 
    font = pygame.font.Font(idef.FONT_FILE_PATH, ROLL_FONT_SIZE)

    # timer
    timer = 0

    # staff roll set
    roll = ["STAFF"]
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("SCENARIO")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("CHARACTER DESIGN")
    roll.append("    Tomo Kanzaki")
    roll.append("")
    roll.append("MAP DESIGN")
    roll.append("    Tomo Kanzaki")
    roll.append("    Mizuki Kita")
    roll.append("    ドット絵世界")
    roll.append("")
    roll.append("BACKGROUND DESIGN")
    roll.append("    きまぐれアフター")
    roll.append("")
    roll.append("MAP EDITOR")
    roll.append("    Mizuki Kita")
    roll.append("")
    roll.append("MAP SYSTEM")
    roll.append("    Koshiro Miyauchi")
    roll.append("    Mizuki Kita")
    roll.append("")
    roll.append("BATTLE SYSTEM")
    roll.append("    Koshiro Miyauchi")
    roll.append("    Madoka Nagai")
    roll.append("")
    roll.append("BATTLE DESIGN")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("PROGRAMMER")
    roll.append("    Koshiro Miyauchi")
    roll.append("    Mizuki Kita")
    roll.append("    Madoka Nagai")
    roll.append("")
    roll.append("SOUND")
    roll.append("    魔王魂")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("SPECIAL THANKS")
    roll.append("    Kei Nishioka")
    roll.append("    ke-ko.ne-ne1.2")
    roll.append("    Kenji Kubota")
    roll.append("    Mika Usuda")
    roll.append("    rintaro")
    roll.append("    yama")
    roll.append("    ぷにぷにバイオ")
    roll.append("    ユーノス・ロードスターNA6CE")
    roll.append("    ゆみしょんしょん")
    roll.append("    井上裕介")
    roll.append("    上野 一輝")
    roll.append("    久後貴寛")
    roll.append("    小野寺英之")
    roll.append("    小林浩")
    roll.append("    川村 一子")
    roll.append("    齋藤純子")
    roll.append("    齋藤真子")
    roll.append("    障子 雄介")
    roll.append("    鈴木いく子")
    roll.append("    高橋浩")
    roll.append("    人見琢也")
    roll.append("    ")
    roll.append("   ※掲載許可をいただけた方のみ")
    roll.append("　　 掲載しております。")
    roll.append("")
    roll.append("    すべての支援者の皆さまに")
    roll.append("    厚く御礼申し上げます。")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("    Gunma University")
    roll.append("    ")
    roll.append("")
    roll.append("")
    roll.append("    academist")
    roll.append("")
    roll.append("")
    roll.append("    ")
    roll.append("DIRECTOR")
    roll.append("    Mizuki Kita")
    roll.append("    Koshiro Miyauchi")
    roll.append("")
    roll.append("")
    roll.append("iGEM Gunma Project Leader (2019)")
    roll.append("    Mizuki Kita")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("")
    roll.append("iGEM Gunma")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg.fill(idef.COLOR_BLACK)
        for i in range(len(roll)):
            posY = idef.WINDOW_HEIGHT - timer + i*30
            if posY < -30 or posY > idef.WINDOW_HEIGHT:
                continue
            idef.TextDraw(bg, roll[i], 50, posY, font, idef.COLOR_WHITE)
        
        timer = timer + 3
        if timer > (len(roll)+8)*30:
            timer = (len(roll)+8)*30
        
        pygame.display.update()
        clk.tick(33)
        
#--------------------------------------------------
# end of file
#--------------------------------------------------

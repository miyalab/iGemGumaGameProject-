'''
Project Name : iGemGunmaGameProject
File Name    : rpg_define.py
Description  : 定数定義ファイル
'''

#----------------------------
# import
#----------------------------
import const
import pygame 

#----------------------------
# window
#----------------------------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE: tuple = (WINDOW_WIDTH,WINDOW_HEIGHT)
WINDOW_NAME: str = 'iGEM RPG GAME'

#----------------------------
# color
#----------------------------
COLOR_BLACK: tuple = (0,0,0)
COLOR_WHITE: tuple = (255,255,255)
COLOR_RED: tuple = (255,0,0)
COLOR_GREEN: tuple = (0,255,0)
COLOR_BLUE: tuple = (0,0,255)

#----------------------------
# key
#----------------------------
KEY_MOVE: int = 0x0f
KEY_UP: int = 0x01
KEY_DOWN: int = 0x02
KEY_LEFT: int = 0x04
KEY_RIGHT: int = 0x08
KEY_SELECT: int = 0x10 
KEY_ENTER: int = 0x20

#----------------------------
# file path
#----------------------------
FONT_FILE_PATH: str = "ipaexg.ttf"
COMMAND_FONT_SIZE: int = 20
MESSAGE_FONT_SIZE: int = 20

#----------------------------
# event define 
#----------------------------
EVENT_OPENING: int = 1

#----------------------------
# player class
#----------------------------
class player():
    Name: str = "name"
    HP: int = 500
    MaxHP: int = 500
    MP: int = 100
    MaxMP: int = 100
    LV: int = 10
    ATK: int = 100
    DEF: int = 100
    INT: int = 10
    AGI: int = 10
    LUK: int = 10
    EXP: int = 10
    Command = ["攻撃"]

#----------------------------
# enemy class
#----------------------------
class enemy():
    def __init__(self):
        Num: int = 0
        ImgPath = "path"
        Name: str = "name"
        HP: int = 0
        MaxHP: int = 0
        MP: int = 0
        MaxMP: int = 0
        LV: int = 0
        ATK: int = 0
        DEF: int = 0
        INT: int = 0
        AGI: int = 0
        LUK: int = 0
        EXP: int = 0

textboxImg = pygame.image.load("img/textbox.100.png")
messageText = [""]*3

#--------------------------------------------------
# text draw function
#--------------------------------------------------
def TextDraw(bg, txt, x, y, fnt, col):
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])

#--------------------------------------------------
# message initialize function
#--------------------------------------------------
def MessageInit():
    for i in range(len(messageText)):
        messageText[i] = ""

#--------------------------------------------------
# message set function
#--------------------------------------------------
def MessageSet(msg: str):
    # すべてのメッセージが埋まっていない場合は後ろに挿入
    for i in range(len(messageText)):
        if messageText[i] == "":
            messageText[i] = msg
            return

    # メッセージが埋まっている場合には1つずつずらす
    for i in range(len(messageText) - 1):
        messageText[i]= messageText[i+1]

    messageText[len(messageText) - 1] = msg

#--------------------------------------------------
# message draw function
#--------------------------------------------------
def MessageDraw(bg, fnt):
    # messagebox show
    bg.blit(textboxImg,[0, WINDOW_HEIGHT - textboxImg.get_height()])

    # message show
    for i in range(len(messageText)):
        TextDraw(bg, messageText[i], 20, WINDOW_HEIGHT - textboxImg.get_height() + 10 + i*30, fnt, COLOR_WHITE)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------
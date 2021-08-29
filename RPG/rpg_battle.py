'''
Project Name : iGemGunmaGameProject
File Name    : rpg_battle.py
Description  : バトルプログラムファイル
'''

#----------------------------
# import
#----------------------------
import pygame
import pygame.locals
import sys
import random
import rpg_define as idef

#----------------------------
# constant value
#----------------------------
TEXT_MARGIN: int = 5

#----------------------------
# global value
#----------------------------
# text data
textboxImg = pygame.image.load("img/textbox.100.png")
commandboxImg = pygame.image.load("img/textbox.150.png")

# player data
playerImg = pygame.image.load("img/battle/e_coli100.png")

# background image data
backgroundImg = pygame.image.load("img/battle/background/roka.jpg")

# enemy data
enemyA: idef.enemy
enemyImg = pygame.image.load("img/battle/enemy/enemy1.png")
enemyNum: int = 0
enemyPosX: int = 0
enemyPosY: int = 0
enemyStep: int = 0
enemyBlink: int = 0

# attack effect data
damageEffect: int = 0
effectImg = pygame.image.load("img/battle/effect/effect_attack.png")

#--------------------------------------------------
# enemy info read function
#--------------------------------------------------
def EnemyRead(_enemy: int) -> idef.enemy:
    global backgroundImg

    enemyData: idef.enemy = idef.enemy()
    if _enemy == 1:
        enemyData.Num = 1
        enemyData.ImgPath = "img/battle/enemy/enemy1.png"
        enemyData.Name = "O157"
        enemyData.MaxHP = 100
        enemyData.HP = 100
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 130
        enemyData.DEF = 70
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

        backgroundImg = pygame.image.load("img/battle/background/BG16b_80.jpg")

    elif _enemy == 2:
        enemyData.Num = 2
        enemyData.ImgPath = "img/battle/enemy/enemy2.png"
        enemyData.Name = "ユーグレナ"
        enemyData.MaxHP = 200
        enemyData.HP = 200
        enemyData.MaxMP = 200
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 130
        enemyData.DEF = 70
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

        backgroundImg = pygame.image.load("img/battle/background/nakaniwa.jpg")

    elif _enemy == 3:
        enemyData.Num = 3
        enemyData.ImgPath = "img/battle/enemy/enemy3.png"
        enemyData.Name = "好熱菌"
        enemyData.MaxHP = 1000
        enemyData.HP = 500
        enemyData.MaxMP = 500
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 130
        enemyData.DEF = 70
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

        backgroundImg = pygame.image.load("img/battle/background/roka.jpg")

    elif _enemy == 4:
        enemyData.Num = 4
        enemyData.ImgPath = "img/battle/enemy/enemy4.png"
        enemyData.Name = "粘菌"
        enemyData.MaxHP = 1000
        enemyData.HP = 500
        enemyData.MaxMP = 500
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 130
        enemyData.DEF = 70
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

        backgroundImg = pygame.image.load("img/battle/background/toshokan.jpg")

    else:
        enemyData.ImgPath = "img/battle/enemy/enemy5.png"
        enemyData.Num = 5
        enemyData.Name = "完全体・O157"
        enemyData.MaxHP = 1000
        enemyData.HP = 1000
        enemyData.MaxMP = 100
        enemyData.MP = 100
        enemyData.LV = 1
        enemyData.ATK = 130
        enemyData.DEF = 70
        enemyData.INT = 100
        enemyData.AGI = 100
        enemyData.LUK = 100
        enemyData.EXP = 1000

        backgroundImg = pygame.image.load("img/battle/background/okujo.jpg")

    return enemyData

#--------------------------------------------------
# battle initialize function
#--------------------------------------------------
def BattleInit(emy:int):
    global enemyA, enemyImg
    enemyA = EnemyRead(emy)
    enemyImg = pygame.image.load(enemyA.ImgPath)

#--------------------------------------------------
# battle screen draw function
#--------------------------------------------------
def BattleDraw(bg, fnt):
    global enemyBlink, damageEffect
    
    bx = 0
    by = 0

    # damage effect process
    if damageEffect > 0:
        damageEffect = damageEffect - 1
        bx = random.randint(-20,20)
        by = random.randint(-10,10)
    bg.blit(backgroundImg, [bx,by])

    # enemy atack scene
    if enemyBlink % 2 == 0 and enemyA.HP > 0:
        bg.blit(enemyImg, [enemyPosX, enemyPosY - enemyStep])

    if enemyBlink > 0:
        enemyBlink = enemyBlink - 1

#--------------------------------------------------
# battle command draw function
#--------------------------------------------------
def BattleCommand(user: idef.player, bg, fnt):
    # command box show
    bg.blit(commandboxImg,[0,idef.WINDOW_HEIGHT - commandboxImg.get_height()])

    # player image show
    bg.blit(playerImg, [25,idef.WINDOW_HEIGHT - commandboxImg.get_height() + 25])

    # Name and HP, MP show
    idef.TextDraw(bg, user.Name, playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 25, fnt, idef.COLOR_WHITE)
    idef.TextDraw(bg, "HP：" + str(user.HP) + "/" + str(user.MaxHP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 50, fnt, idef.COLOR_WHITE)
    idef.TextDraw(bg, "MP：" + str(user.MP) + "/" + str(user.MaxMP), playerImg.get_width() + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 75, fnt, idef.COLOR_WHITE)

    # command show
    for i in range(len(user.Command)):
        idef.TextDraw(bg, "[" + str(i+1) + "] " + user.Command[i], idef.WINDOW_WIDTH/2 + 50, idef.WINDOW_HEIGHT - commandboxImg.get_height() + 18 + i*30, fnt, idef.COLOR_WHITE)

#--------------------------------------------------
# battle main function
#--------------------------------------------------
def BattleMain(scr, clk, user: idef.player, emyNum: int):
    # enable change global value 
    global enemyA, enemyImg
    global enemyPosX, enemyPosY
    global enemyStep, damageEffect
    
    # local value
    timer: int = 0
    scene: int = 0
    damage: int = 0

    # font set
    commandFont = pygame.font.Font(idef.FONT_FILE_PATH, idef.COMMAND_FONT_SIZE)
    messageFont = pygame.font.Font(idef.FONT_FILE_PATH, idef.MESSAGE_FONT_SIZE)

    # key input setup
    pygame.key.set_repeat()

    # read enemy data
    enemyA = EnemyRead(emyNum)
    enemyImg = pygame.image.load(enemyA.ImgPath)
    enemyPosX = idef.WINDOW_WIDTH/2 - enemyImg.get_width()/2
    enemyPosY = idef.WINDOW_HEIGHT/2 - enemyImg.get_height()

    while scene >= 0:
        # event skip
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # game state update
        BattleDraw(scr, messageFont)
        key = pygame.key.get_pressed()
        timer = timer + 1

        # battle start
        if scene == 0:
            idef.MessageInit()
            idef.MessageSet(enemyA.Name + "があらわれた．");
            scene = 1

        elif scene == 1:
            # Messagebox show
            idef.MessageDraw(scr, messageFont)

            # wait space input
            if key[pygame.locals.K_SPACE] == 1:
                # user input state scene
                scene = 11

        # user input state
        elif scene == 11:
            idef.MessageInit()
            scene = 12

        # wait player input
        elif scene == 12:
            # command show
            BattleCommand(user, scr, commandFont)

            # wait command secelt
            if(key[pygame.locals.K_1] == 1):
                idef.MessageSet(str(user.Name) + "の攻撃")
                damage = int(user.ATK - enemyA.DEF + random.randint(0, 30))
                if damage < 0: damage = 0
                if damage > 9999: damage = 9999
                scene = 21
                timer = 0
            elif(key[pygame.locals.K_2] == 1 and len(user.Command)>=2) and user.MP >= 10:
                idef.MessageSet(str(user.Name) + "の" + user.Command[1] + "による攻撃")
                damage = int(user.ATK * 1.2 - enemyA.DEF + random.randint(0, 50))
                if damage < 0: damage = 0
                if damage > 9999: damage = 9999
                user.MP = user.MP - 10
                scene = 22
                timer = 0
            elif(key[pygame.locals.K_3] == 1 and len(user.Command)>=3) and user.MP >= 20:
                idef.MessageSet(str(user.Name) + "の" + user.Command[2] + "による攻撃")
                damage = int(user.ATK * 1.5 - enemyA.DEF + random.randint(0, 100))
                if damage < 0: damage = 0
                if damage > 9999: damage = 9999
                user.MP = user.MP - 20
                scene = 23
                timer = 0
            elif(key[pygame.locals.K_4] == 1 and len(user.Command)>=4) and user.MP >= 30:
                idef.MessageSet(str(user.Name) + "の" + user.Command[3] + "による攻撃")
                damage = int(user.ATK * 2.0 - enemyA.DEF + random.randint(0, 150))
                if damage < 0: damage = 0
                if damage > 9999: damage = 9999
                user.MP = user.MP - 30
                scene = 24
                timer = 0

        # [1] 攻撃エフェクト
        elif scene == 21:
            idef.MessageDraw(scr, messageFont)
            if 2 == timer or timer == 4:
                scr.fill(idef.COLOR_WHITE)
                #scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                idef.MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [2] コマンドエフェクト
        elif scene == 22:
            idef.MessageDraw(scr, messageFont)
            if 2 == timer or timer == 4:
                scr.fill(idef.COLOR_GREEN)
                #scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                idef.MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [3] コマンドエフェクト
        elif scene == 23:
            idef.MessageDraw(scr, messageFont)
            if 2 == timer or timer == 4:
                scr.fill(idef.COLOR_ORANGE)
                #scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                idef.MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # [4] コマンドエフェクト
        elif scene == 24:
            idef.MessageDraw(scr, messageFont)
            if 2 == timer or timer == 4:
                scr.fill(idef.COLOR_BLUE)
                #scr.blit(effectImg, [400-timer*60, -100+timer*60])

            if timer == 5:
                enemyBlink = 5
                idef.MessageSet(enemyA.Name + "は" + str(damage) + "のダメージ")
                enemyA.HP = enemyA.HP - damage
                if(enemyA.HP <= 0):
                    scene = 51

            if timer >= 16 and key[pygame.locals.K_SPACE] == 1:
                scene = 31
                timer = 0

        # エネミーからの攻撃
        elif scene == 31:
            idef.MessageInit()
            idef.MessageSet(enemyA.Name + "からの攻撃")
            damage = enemyA.ATK - user.DEF + random.randint(0,5)
            if damage < 0: damage = 0
            scene = 32

        # エネミーから攻撃エフェクト
        elif scene == 32:
            idef.MessageDraw(scr, messageFont)
            if timer == 5:
                enemyStep = 30
            if timer == 9:
                idef.MessageSet(user.Name + "は" + str(damage) + "のダメージ")
                user.HP = user.HP - damage
                if(user.HP <= 0):
                    scene = 101
                damageEffect = 5
                enemyStep = 0
            if timer >= 20 and key[pygame.locals.K_SPACE] == 1:
                scene = 11
                timer = 0

        # エネミーを撃破
        elif scene == 51:
            idef.MessageDraw(scr, messageFont)
            idef.MessageSet(user.Name + "は" + enemyA.Name + "を撃破した．")
            scene = 52

        # エネミー撃破後のキー入力待ち
        elif scene ==52:
            idef.MessageDraw(scr, messageFont)
            if key[pygame.locals.K_SPACE] == 1:
                # key input setup
                pygame.key.set_repeat(1,1)
                scene = -1

        # プレイヤー敗北
        elif scene == 101:
            idef.MessageDraw(scr, messageFont)
            idef.MessageSet(user.Name + "は敗北した．")
            idef.MessageSet("ゲームを再開するには再起動してください．")
            scene = 102

        # プレイヤー敗北後のキー入力待ち
        elif scene == 102:
            idef.MessageDraw(scr, messageFont)

        pygame.display.update()
        clk.tick(10)
        
#--------------------------------------------------
# end of file
#--------------------------------------------------

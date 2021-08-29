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
import rpg_define as idef
import rpg_battle as ibattle
import rpg_staffroll as iroll

#----------------------------
# constant value
#----------------------------
MAP_IMG_ITEM: int = 1000

DIR_L: int = -1
DIR_R: int = -2
DIR_U: int = 1
DIR_D: int = 2

soundWalk = pygame.mixer.Sound("sound/ashioto.ogg")
bgmMAP = pygame.mixer.music.load("sound/op2.ogg")
charImg = pygame.image.load("img/player/front/C-13.PNG")

frontImg = [pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-2.PNG"),
            pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-4.PNG"),
            pygame.image.load("img/player/front/C-13.PNG"),
            pygame.image.load("img/player/front/C-2.PNG")]
sideImg = [pygame.image.load("img/player/side/Cs-1.PNG"),
           pygame.image.load("img/player/side/Cs-2.PNG"),
           pygame.image.load("img/player/side/Cs-3.PNG"),
           pygame.image.load("img/player/side/Cs-4.PNG"),
           pygame.image.load("img/player/side/Cs-3.PNG"),
           pygame.image.load("img/player/side/Cs-2.PNG")]
mapImg = [pygame.image.load("img/map/clear.PNG"),
          pygame.image.load("img/map/t01.PNG"),
          pygame.image.load("img/map/t02.PNG"),
          pygame.image.load("img/map/t03.PNG"),
          pygame.image.load("img/map/t04.PNG"),
          pygame.image.load("img/map/t05.PNG"),
          pygame.image.load("img/map/t06.PNG"),
          pygame.image.load("img/map/t07.PNG"),
          pygame.image.load("img/map/t08.PNG"),
          pygame.image.load("img/map/t09.PNG"),
          pygame.image.load("img/map/t10.PNG"),
          pygame.image.load("img/map/t11.PNG"),
          pygame.image.load("img/map/t12.PNG"),
          pygame.image.load("img/map/t13.PNG"),
          pygame.image.load("img/map/t14.PNG"),
          pygame.image.load("img/map/t15.PNG"),
          pygame.image.load("img/map/t16.PNG"),
          pygame.image.load("img/map/t17.PNG"),
          pygame.image.load("img/map/t18.PNG"),
          pygame.image.load("img/map/t19.PNG"),
          pygame.image.load("img/map/t20.PNG"),
          pygame.image.load("img/map/t21.PNG"),
          pygame.image.load("img/map/t22.PNG"),
          pygame.image.load("img/map/t23.PNG"),
          pygame.image.load("img/map/t24.PNG"),
          pygame.image.load("img/map/t25.PNG"),
          pygame.image.load("img/map/t26.PNG"),
          pygame.image.load("img/map/t27.PNG"),
          pygame.image.load("img/map/t28.PNG"),
          pygame.image.load("img/map/t29.PNG"),
          pygame.image.load("img/map/t30.PNG"),
          pygame.image.load("img/map/t31.PNG"),
          pygame.image.load("img/map/t32.PNG"),
          pygame.image.load("img/map/t33.PNG"),
          pygame.image.load("img/map/t34.PNG"),
          pygame.image.load("img/map/t35.PNG"),
          pygame.image.load("img/map/t36.PNG"),
          pygame.image.load("img/map/t37.PNG"),
          pygame.image.load("img/map/t38.PNG"),
          pygame.image.load("img/map/t39.PNG"),
          pygame.image.load("img/map/t40.PNG"),
          pygame.image.load("img/map/t41.PNG"),
          pygame.image.load("img/map/t42.PNG"),
          pygame.image.load("img/map/t43.PNG"),
          pygame.image.load("img/map/t44.PNG"),
          pygame.image.load("img/map/t45.PNG"),
          pygame.image.load("img/map/t46.PNG"),
          pygame.image.load("img/map/t47.PNG"),
          pygame.image.load("img/map/t48.PNG"),
          pygame.image.load("img/map/t49.PNG"),
          pygame.image.load("img/map/t50.PNG"),
          pygame.image.load("img/map/t51.PNG"),
          pygame.image.load("img/map/t52.PNG"),
          pygame.image.load("img/map/t53.PNG"),
          pygame.image.load("img/map/t54.PNG"),
          pygame.image.load("img/map/t55.PNG"),
          pygame.image.load("img/map/t56.PNG"),
          pygame.image.load("img/map/t57.PNG"),
          pygame.image.load("img/map/t58.PNG"),
          pygame.image.load("img/map/t59.PNG"),
          pygame.image.load("img/map/t60.PNG"),
          pygame.image.load("img/map/t61.PNG"),
          pygame.image.load("img/map/t62.PNG"),
          pygame.image.load("img/map/t63.PNG"),
          pygame.image.load("img/map/t64.PNG"),
          pygame.image.load("img/map/t65.PNG"),
          pygame.image.load("img/map/t66.PNG"),
          pygame.image.load("img/map/t67.PNG"),
          pygame.image.load("img/map/t68.PNG"),
          pygame.image.load("img/map/t69.PNG"),
          pygame.image.load("img/map/t70.PNG"),
          pygame.image.load("img/map/t71.PNG"),
          pygame.image.load("img/map/t72.PNG"),
          pygame.image.load("img/map/t73.PNG"),
          pygame.image.load("img/map/t74.PNG"),
          pygame.image.load("img/map/t75.PNG"),
          pygame.image.load("img/map/t76.PNG"),
          pygame.image.load("img/map/t77.PNG"),
          pygame.image.load("img/map/t78.PNG"),
          pygame.image.load("img/map/t79.PNG"),
          pygame.image.load("img/map/t80.PNG"),
          pygame.image.load("img/map/t81.PNG"),
          pygame.image.load("img/map/t82.PNG"),
          pygame.image.load("img/map/t83.PNG"),
          pygame.image.load("img/map/t84.PNG"),
          pygame.image.load("img/map/t85.PNG"),
          pygame.image.load("img/map/t86.PNG"),
          pygame.image.load("img/map/t87.PNG"),
          pygame.image.load("img/map/t88.PNG"),
          pygame.image.load("img/map/t89.PNG"),
          pygame.image.load("img/map/t90.PNG"),
          pygame.image.load("img/map/t91.PNG"),
          pygame.image.load("img/map/t92.PNG"),
          pygame.image.load("img/map/t93.PNG"),
          pygame.image.load("img/map/t94.PNG"),
          pygame.image.load("img/map/t95.PNG"),
          pygame.image.load("img/map/t96.PNG"),
          pygame.image.load("img/map/t97.PNG"),
          pygame.image.load("img/map/t98.PNG"),
          pygame.image.load("img/map/t99.PNG"),
          pygame.image.load("img/map/t100.PNG"),
          pygame.image.load("img/map/t101.PNG"),
          pygame.image.load("img/map/t102.PNG"),
          pygame.image.load("img/map/t103.PNG"),
          pygame.image.load("img/map/t104.PNG"),
          pygame.image.load("img/map/t105.PNG"),
          pygame.image.load("img/map/t106.PNG"),
          pygame.image.load("img/map/t107.PNG"),
          pygame.image.load("img/map/t108.PNG"),
          pygame.image.load("img/map/t109.PNG"),
          pygame.image.load("img/map/t110.PNG"),
          pygame.image.load("img/map/t111.PNG"),
          pygame.image.load("img/map/t112.PNG"),
          pygame.image.load("img/map/t113.PNG"),
          pygame.image.load("img/map/t114.PNG"),
          pygame.image.load("img/map/t115.PNG")]
overMapImg = [pygame.image.load("img/map/clear.PNG"),
              pygame.image.load("img/map/a01.PNG"),
              pygame.image.load("img/map/a02.PNG"),
              pygame.image.load("img/map/a03.PNG"),
              pygame.image.load("img/map/a04.PNG"),
              pygame.image.load("img/map/a05.PNG"),
              pygame.image.load("img/map/a06.PNG"),
              pygame.image.load("img/map/a07.PNG"),
              pygame.image.load("img/map/a08.PNG"),
              pygame.image.load("img/map/a09.PNG"),
              pygame.image.load("img/map/a10.PNG"),
              pygame.image.load("img/map/a11.PNG"),
              pygame.image.load("img/map/a12.PNG"),
              pygame.image.load("img/map/a13.PNG"),
              pygame.image.load("img/map/a14.PNG"),
              pygame.image.load("img/map/a15.PNG"),
              pygame.image.load("img/map/a16.PNG"),
              pygame.image.load("img/map/a17.PNG"),
              pygame.image.load("img/map/a18.PNG"),
              pygame.image.load("img/map/a19.PNG"),
              pygame.image.load("img/map/a20.PNG"),
              pygame.image.load("img/map/a21.PNG"),
              pygame.image.load("img/map/a22.PNG"),
              pygame.image.load("img/map/a23.PNG"),
              pygame.image.load("img/map/a24.PNG"),
              pygame.image.load("img/map/a25.PNG"),
              pygame.image.load("img/map/a26.PNG"),
              pygame.image.load("img/map/a27.PNG"),
              pygame.image.load("img/map/a28.PNG"),
              pygame.image.load("img/map/a29.PNG"),
              pygame.image.load("img/map/a30.PNG"),
              pygame.image.load("img/map/a31.PNG"),
              pygame.image.load("img/map/a32.PNG"),
              pygame.image.load("img/map/a33.PNG"),
              pygame.image.load("img/map/a34.PNG"),
              pygame.image.load("img/map/a35.PNG"),
              pygame.image.load("img/map/a36.PNG"),
              pygame.image.load("img/map/a37.PNG"),
              pygame.image.load("img/map/a38.PNG"),
              pygame.image.load("img/map/a39.PNG"),
              pygame.image.load("img/map/a40.PNG"),
              pygame.image.load("img/map/a41.PNG"),
              pygame.image.load("img/map/a42.PNG"),
              pygame.image.load("img/map/a43.PNG"),
              pygame.image.load("img/map/a44.PNG"),
              pygame.image.load("img/map/a45.PNG"),
              pygame.image.load("img/map/a46.PNG"),
              pygame.image.load("img/map/a47.PNG"),
              pygame.image.load("img/map/a48.PNG"),
              pygame.image.load("img/map/a49.PNG"),
              pygame.image.load("img/map/a50.PNG"),
              pygame.image.load("img/map/a51.PNG"),
              pygame.image.load("img/map/a52.PNG"),
              pygame.image.load("img/map/a53.PNG"),
              pygame.image.load("img/map/a54.PNG"),
              pygame.image.load("img/map/a55.PNG"),
              pygame.image.load("img/map/a56.PNG"),
              pygame.image.load("img/map/a57.PNG"),
              pygame.image.load("img/map/a58.PNG"),
              pygame.image.load("img/map/a59.PNG"),
              pygame.image.load("img/map/a60.PNG"),
              pygame.image.load("img/map/a61.PNG"),
              pygame.image.load("img/map/a62.PNG"),
              pygame.image.load("img/map/a63.PNG"),
              pygame.image.load("img/map/a64.PNG"),
              pygame.image.load("img/map/a65.PNG"),
              pygame.image.load("img/map/a66.PNG"),
              pygame.image.load("img/map/a67.PNG"),
              pygame.image.load("img/map/a68.PNG"),
              pygame.image.load("img/map/a69.PNG"),
              pygame.image.load("img/map/a70.PNG"),
              pygame.image.load("img/map/a71.PNG"),
              pygame.image.load("img/map/a72.PNG"),
              pygame.image.load("img/map/a73.PNG"),
              pygame.image.load("img/map/a74.PNG"),
              pygame.image.load("img/map/a75.PNG"),
              pygame.image.load("img/map/a76.PNG"),
              pygame.image.load("img/map/a77.PNG"),
              pygame.image.load("img/map/a78.PNG"),
              pygame.image.load("img/map/a79.PNG"),
              pygame.image.load("img/map/a80.PNG"),
              pygame.image.load("img/map/a81.PNG"),
              pygame.image.load("img/map/a82.PNG"),
              pygame.image.load("img/map/a83.PNG"),
              pygame.image.load("img/map/a84.PNG"),
              pygame.image.load("img/map/a85.PNG"),
              pygame.image.load("img/map/a86.PNG"),
              pygame.image.load("img/map/a87.PNG"),
              pygame.image.load("img/map/a88.PNG"),
              pygame.image.load("img/map/a89.PNG"),
              pygame.image.load("img/map/a90.PNG"),
              pygame.image.load("img/map/a91.PNG"),
              pygame.image.load("img/map/a92.PNG"),
              pygame.image.load("img/map/a93.PNG"),
              pygame.image.load("img/map/a94.PNG"),
              pygame.image.load("img/map/a95.PNG"),
              pygame.image.load("img/map/a96.PNG"),
              pygame.image.load("img/map/a97.PNG"),
              pygame.image.load("img/map/a98.PNG"),
              pygame.image.load("img/map/a99.PNG"),
              pygame.image.load("img/map/a100.PNG"),
              pygame.image.load("img/map/a101.PNG"),
              pygame.image.load("img/map/a102.PNG"),
              pygame.image.load("img/map/a103.PNG"),
              pygame.image.load("img/map/a104.PNG"),
              pygame.image.load("img/map/a105.PNG"),
              pygame.image.load("img/map/a106.PNG"),
              pygame.image.load("img/map/a107.PNG"),
              pygame.image.load("img/map/a108.PNG"),
              pygame.image.load("img/map/a109.PNG"),
              pygame.image.load("img/map/a110.PNG"),
              pygame.image.load("img/map/a111.PNG"),
              pygame.image.load("img/map/a112.PNG"),
              pygame.image.load("img/map/a113.PNG"),
              pygame.image.load("img/map/a114.PNG"),
              pygame.image.load("img/map/a115.PNG"),
              pygame.image.load("img/map/a116.PNG"),
              pygame.image.load("img/map/a117.PNG"),
              pygame.image.load("img/map/a118.PNG"),
              pygame.image.load("img/map/a119.PNG"),
              pygame.image.load("img/map/a120.PNG"),
              pygame.image.load("img/map/a121.PNG"),
              pygame.image.load("img/map/a122.PNG"),
              pygame.image.load("img/map/a123.PNG"),
              pygame.image.load("img/map/a124.PNG"),
              pygame.image.load("img/map/a125.PNG"),
              pygame.image.load("img/map/a126.PNG"),
              pygame.image.load("img/map/a127.PNG"),
              pygame.image.load("img/map/a128.PNG"),
              pygame.image.load("img/map/a129.PNG"),
              pygame.image.load("img/map/a130.PNG"),
              pygame.image.load("img/map/a131.PNG"),
              pygame.image.load("img/map/a132.PNG"),
              pygame.image.load("img/map/a133.PNG"),
              pygame.image.load("img/map/a134.PNG"),
              pygame.image.load("img/map/a135.PNG"),
              pygame.image.load("img/map/a136.PNG"),
              pygame.image.load("img/map/a137.PNG"),
              pygame.image.load("img/map/a138.PNG"),
              pygame.image.load("img/map/a139.PNG"),
              pygame.image.load("img/map/a140.PNG"),
              pygame.image.load("img/map/a141.PNG"),
              pygame.image.load("img/map/a142.PNG"),
              pygame.image.load("img/map/a143.PNG"),
              pygame.image.load("img/map/a144.PNG"),
              pygame.image.load("img/map/a145.PNG"),
              pygame.image.load("img/map/a146.PNG"),
              pygame.image.load("img/map/a147.PNG"),
              pygame.image.load("img/map/a148.PNG"),
              pygame.image.load("img/map/a149.PNG"),
              pygame.image.load("img/map/a150.PNG"),
              pygame.image.load("img/map/a151.PNG"),
              pygame.image.load("img/map/a152.PNG"),
              pygame.image.load("img/map/a153.PNG"),
              pygame.image.load("img/map/a154.PNG"),
              pygame.image.load("img/map/a155.PNG"),
              pygame.image.load("img/map/a156.PNG"),
              pygame.image.load("img/map/a157.PNG"),
              pygame.image.load("img/map/a158.PNG"),
              pygame.image.load("img/map/a159.PNG"),
              pygame.image.load("img/map/a160.PNG"),
              pygame.image.load("img/map/a161.PNG"),
              pygame.image.load("img/map/a162.PNG"),
              pygame.image.load("img/map/a163.PNG"),
              pygame.image.load("img/map/a164.PNG"),
              pygame.image.load("img/map/a165.PNG"),
              pygame.image.load("img/map/a166.PNG"),
              pygame.image.load("img/map/a167.PNG"),
              pygame.image.load("img/map/a168.PNG"),
              pygame.image.load("img/map/a169.PNG"),
              pygame.image.load("img/map/a170.PNG"),
              pygame.image.load("img/map/a171.PNG"),
              pygame.image.load("img/map/a172.PNG"),
              pygame.image.load("img/map/a173.PNG"),
              pygame.image.load("img/map/a174.PNG"),
              pygame.image.load("img/map/a175.PNG"),
              pygame.image.load("img/map/a176.PNG"),
              pygame.image.load("img/map/a177.PNG"),
              pygame.image.load("img/map/a178.PNG"),
              pygame.image.load("img/map/a179.PNG"),
              pygame.image.load("img/map/a180.PNG"),
              pygame.image.load("img/map/a181.PNG"),
              pygame.image.load("img/map/a182.PNG"),
              pygame.image.load("img/map/a183.PNG"),
              pygame.image.load("img/map/a184.PNG"),
              pygame.image.load("img/map/a185.PNG"),
              pygame.image.load("img/map/a186.PNG"),
              pygame.image.load("img/map/a187.PNG"),
              pygame.image.load("img/map/a188.PNG"),
              pygame.image.load("img/map/a189.PNG"),
              pygame.image.load("img/map/a190.PNG"),
              pygame.image.load("img/map/a191.PNG"),
              pygame.image.load("img/map/a192.PNG"),
              pygame.image.load("img/map/a193.PNG"),
              pygame.image.load("img/map/a194.PNG"),
              pygame.image.load("img/map/a195.PNG"),
              pygame.image.load("img/map/a196.PNG"),
              pygame.image.load("img/map/a197.PNG"),
              pygame.image.load("img/map/a198.PNG"),
              pygame.image.load("img/map/a199.PNG"),
              pygame.image.load("img/map/a200.PNG"),
              pygame.image.load("img/map/a201.PNG"),
              pygame.image.load("img/map/a202.PNG"),
              pygame.image.load("img/map/a203.PNG"),
              pygame.image.load("img/map/a204.PNG"),
              pygame.image.load("img/map/a205.PNG"),
              pygame.image.load("img/map/a206.PNG"),
              pygame.image.load("img/map/a207.PNG"),
              pygame.image.load("img/map/a208.PNG"),
              pygame.image.load("img/map/a209.PNG"),
              pygame.image.load("img/map/a210.PNG"),
              pygame.image.load("img/map/a211.PNG"),
              pygame.image.load("img/map/a212.PNG"),
              pygame.image.load("img/map/a213.PNG"),
              pygame.image.load("img/map/a214.PNG"),
              pygame.image.load("img/map/a215.PNG"),
              pygame.image.load("img/map/a216.PNG"),
              pygame.image.load("img/map/a217.PNG"),
              pygame.image.load("img/map/a218.PNG"),
              pygame.image.load("img/map/a219.PNG")]

mapNum = -1
mapNow = [[]]

posX: int = 0
posY: int = 0
dir: int = 0
dirChar: int = 0
charShowFlag: int = 0

#--------------------------------------------------
# Map Data Load function
#--------------------------------------------------
def MapLoad(_map: int):
    ret = [[]]
    ret.clear()
    
        #1,2,3は人
        #4は図書館の看板　　「このさき　かいそうちゅう　とおれません」　と　かいてある。
        #5　「じっけんきぐ　は　たいせつに　あつかおう」とかいてある。
        #6　「オートクレーブ」　と　かいてある……。もう　あっちへ　いこう。
        #7は70%エタノール　「7エタ」　と　かいてある。なんだか　いやな　かんじが　する。
        #8はあひる　かわいい　あひるが　ある。
        #9はイベントが起こらない、ただの物とかを通れなくする

    # map 
    if _map == 0:
        ret.append([9000030,57054030,9201030,9000030,58102030,9000000,9000000,9000000,9000030,9201030,9042030,9201030,52004030,9000030,9000000,9000000,9000000,9000000,9212030,9056030,90174030,9201030,9000030,5004030,9000030,9201030,9000030,9206030])
        ret.append([214054,54,9073054,90112054,54,9000000,9000000,9000000,54,9072054,51210054,61054,54,54,9000000,9000000,9000000,9000000,213054,54,61054,54,2002054,54,54,54,6014054,9207054])
        ret.append([215054,54,111054,113054,43054,9000000,9000000,9000000,54,111054,113054,54,1001054,54,9000000,9000000,9000000,9000000,54,75078054,9069054,54,9077054,9146054,54,73080054,7071054,54])
        ret.append([216054,56144054,55146054,54,54,9000000,9000000,9000000,54,54,29054,54,54144054,53146054,9000000,9000000,9000000,9000000,9045054,111054,113054,9045054,111054,147054,54,111054,113054,9204054])
        ret.append([54,145054,147054,54,54,9000000,9000000,9000000,54,3003054,54,54,145054,147054,9000000,9000000,9000000,9000000,9041054,61054,43054,54,54,54,54,43054,54,76205054])
        ret.append([54,29054,54,54,54,9000000,9000000,9000000,54,54,54,54,43054,54,9000000,9000000,000000,9000000,54,9073054,9208054,54,9144054,9146054,54,9077054,9211054,54])
        ret.append([9000000,9000000,9000000,54,9000000,9000000,9000000,9000000,9000000,9000000,54,9000000,9000000,9000000,9000000,9000000,9000000,9000000,54,111054,113054,54,145054,147054,54,111054,113054,9204054])
        ret.append([54,54,54,54,54,54,54,54,9048054,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,61054,77205054])
        ret.append([54,54,54,54,54,54,54,54,54,54,54,32054,46054,54,54,54,54,54,54,54,54,54,54,54,54,54,54,71055054])
        ret.append([9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9064036,103036,63036,9000000,9000000,9000000,9000000,9000000,54,72079054,7071054,54,73080054,74209054,54,9076054,9112054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,36,36036,9000000,0,0,0,0,9000000,54,111054,113054,54,111054,113054,54,111054,113054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,60,59,9000000,0,0,0,0,9000000,54,54,54,54,54,54,54,54,43054,54])
        ret.append([0,0,0,0,0,0,0,0,0,9000000,0,0,9000000,0,0,0,0,9000000,9000000,9000000,9000000,9000000,9000000,9000000])

    elif _map == 1:
        ret.append([115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114,115,115,115,114])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,9000107,9000109,9000109,9000109,9000109,9000111,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,51038,51038,51038,38,51038,38,51038,38,9000004,5,5,5,5,9000006,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38])
        ret.append([38,38,39,39,127038,38,38,38,38,38,51038,38,38,38,51038,38,51038,38,9000004,5,5,5,5,9000006,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38])
        ret.append([38,38,38,39,39,38,127038,38,38,38,51038,38,51038,38,51038,38,51038,38,9000004,5,5,5,5,9000006,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38])
        ret.append([38,38,38,38,39,39,39,38,38,38,51038,51038,51038,38,51038,51038,51038,38,9000004,5,5,5,5,9000006,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38,38,39,39,39,38,38])
        ret.append([38,38,38,38,38,127038,39,39,38,38,129038,129038,129038,129038,129038,129038,129038,129038,9000004,9000005,5,5,5,9000006,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,39,38,38,38,38,38,38,38,38])
        ret.append([38,38,98,9000061,9000063,98,38,39,39,39,39,39,39,39,39,39,39,39,7,9000008,8,8,8,9000009,39,39,38,38,38,38,38,38,38,38,38,38,38,39,39,43,9000107,9000109,9000109,9000109,9000109,9000109,9000111,38])
        ret.append([38,38,126038,9000062,9000064,127038,38,39,39,39,39,39,39,39,39,39,39,39,30,9000030,30,30,30,9000030,39,39,38,9000107,9000109,9000109,9000109,9000109,9000109,9000109,9000109,9000109,9000111,44,39,43,9000004,5,5,5,5,5,9000006,38])
        ret.append([38,38,38,38,98,38,39,39,38,38,129038,129038,129038,39,39,129038,90193038,129038,9000030,30,30,30,30,9000030,39,39,38,9000004,5,5,5,5,5,5,5,5,9000006,44,39,43,9000004,5,5,5,5,5,9000006,38])
        ret.append([38,9128038,38,38,38,9128038,39,39,38,38,38,38,38,39,39,38,81194038,38,9000030,9000030,9000030,9000030,9037030,9000030,39,39,38,9000007,8,8,8,8,8,8,8,8,9000009,44,39,43,9000007,8,8,8,8,8,9000009,38])
        ret.append([38,38,38,9128038,9130038,9132038,38,39,39,38,38,38,38,39,39,38,9028038,38,38,38,38,9039038,38038,38,39,39,38,9000031,31,31,31,31,31,31,31,31,9000031,44,39,43,9000018,17,16,17,16,17,9000019,38])
        ret.append([38,38,38,38,131038,133038,129038,39,39,39,38,38,38,39,39,38,38,38,38,38,9028038,38,38,38,39,39,38,9000031,9195031,195031,9000031,9000031,9000031,195031,196031,9000031,9000031,44,39,43,9000018,9000016,9000016,9000016,9000016,9000016,9000019,38])
        ret.append([38,38,38,38,38,38,38,38,39,39,39,38,38,39,39,38,38,9028038,38,38,38,38,38,38,39,39,38,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,9000031,44,39,43,9000018,9000017,9000016,9000017,9000016,9000017,9000019,38])
        ret.append([38,38,38,38,38,38,38,38,38,39,39,39,39,39,39,38,38,38,38,38,38,38,38,38,39,39,38,9000030,9000030,9000030,9000030,105,106,9000030,9000030,9000030,9000030,44,39,43,9000018,9000016,9000016,9000016,9000016,9000016,9000019,38])
        ret.append([38,38,9000107,9000109,9000109,9000109,9000109,9000109,9000109,9000110,9000110,9000110,9000112,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38,9005038,38,9005038,38,38,9027038,38,9027038,38,39,39,43,9000018,9000016,9000016,20,9000016,9000016,9000019,38])
        ret.append([38,38,9000004,5,5,5,5,5,5,5,5,5,9000006,38,38,39,39,38,38,9000107,9000109,9000109,9000109,9148109,9000111,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,47,47,47,47,47,47,47,38])
        ret.append([38,38,9000007,8,8,8,8,8,8,8,8,8,9000009,38,38,39,39,38,38,9000004,5,5,5,104,9000006,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38])
        ret.append([38,38,9000031,31,31,31,31,31,31,31,31,31,9000031,38,38,39,39,38,38,9000004,5,5,5,5,9000006,38,39,9000108,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000110,9000112,39,39,39,38])
        ret.append([38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,38,38,39,39,38,38,9000004,5,5,5,5,9000006,38,38,9000004,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,9000006,38,38,38,38])
        ret.append([38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,38,38,39,39,38,38,9000007,9000008,9000008,9000008,9000008,9000009,38,38,9000004,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,9000006,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,38,38,9000027,9000034,9000034,9000034,34,9000027,38,38,9000007,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9000009,38,38,38,38])
        ret.append([38,51038,38,51038,51038,51038,38,51038,51038,51038,38,51038,38,51038,38,39,39,38,38,9000034,9000027,34,34,27,9000034,38,38,9000031,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,9000031,38,38,38,38])
        ret.append([38,38,38,51038,38,38,38,51038,51038,38,38,51038,51038,51038,38,39,39,38,38,9000034,9000034,27,27,34,9000034,38,38,9000031,195031,196031,31,31,31,195031,9196031,9000031,9195031,9196031,31,31,31,9195031,9196031,9000031,38,38,38,38])
        ret.append([38,51038,38,51038,38,51038,38,51038,51038,38,38,51038,38,51038,38,39,39,38,38,9000034,9000034,27,27,34,9000034,38,38,9000031,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,9000031,38,38,38,38])
        ret.append([38,51038,38,51038,51038,51038,38,51038,51038,51038,38,51038,38,51038,38,39,39,38,38,9000034,9000027,9000034,9000034,9000027,9000034,38,38,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,9195031,9196031,9000031,9000031,9000031,9195031,9196031,9000031,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,39,39,38,38,9000027,9000034,9000034,106,9000034,9000027,38,38,9000031,9000031,9000031,9000031,9000031,9000031,9000031,9000031,105,9000031,820218031,9219031,9000031,9000031,9000031,9000031,9000031,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,9022038,38,9022038,38,38,38,38,38,38,38,38,38,38,38])
        ret.append([38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38])

    elif _map == 2:
        ret.append([9154100,9156100,9000000,0,0,0,0,0])   
        ret.append([9155100,9157100,0,0,9000000,0,0,0])
        ret.append([100,100,60,59,9000000,9000000,9000000,9000000])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100])
        ret.append([100,100,100,100,178100,180100])
        ret.append([100,100,107100,109100,9179100,9181100])
        ret.append([9000000,9000000,0,0,9000000,9000000])

    elif _map == 3:
        ret.append([9000030,9000030,9098030,9000030,9056030,9057030,9000000,0,0,0,0,0,0,0,0,0])
        ret.append([100,100,100,100,100,100])
        ret.append([9082100,9085100,9067100,9091100,9094100,100,9000000,0,0,0,0,0,0,0,0,0])
        ret.append([9083100,9086100,9099100,92100,95100,100,9000000,0,0,0,100,100,0,0,0,0])
        ret.append([84100,87100,90100,93100,96100,100,9000067,9000072,9000072,9000069,9081100,4191100,0,0,0,0])
        ret.append([100,100,100,100,100,100,9000071,75,75,9000074,100,192100,9000000,0,0,0])
        ret.append([91161100,92163100,94184100,100,100,9169100,90000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([162100,164100,185100,100,175100,9170100,9000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([93161100,93163100,100,100,176100,9171100,9000071,75,75,9000074,100,100,9000000,0,0,0])
        ret.append([162100,164100,61100,100,177100,9172100,9000068,9000073,9000073,9000070,100,100,9000000,9000000,9000000,9000000])
        ret.append([100,100,100,100,100,100,9000030,9000030,9000030,9000030,100,100,9000030,9102030,9174030,9000030])
        ret.append([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100])
        ret.append([9000067,9000072,9000072,9000069,100,100,100,100,100,100,100,100,100,9074100,100,100])
        ret.append([71,75,75,9000074,9037030,9054030,9000030,90097030,9000030,100,100,100,100,9075100,173100,100])
        ret.append([71,75,75,9000074,38100,39100,100,100,100,100,100,100,100,9068100,100,100])
        ret.append([71,75,75,9000074,100,100,100100,9104100,100,9166100,100,100,100,9065100,173100,100])
        ret.append([71,75,75,9000074,90167100,100,9104100,101100,100,9165100,100,100,100,90190100,100,100])
        ret.append([68,73,73,9000070,9000021,9000021,9000021,9000021,9000021,9000000,107100,109100,9000000,9000000,9000000,9000000])
        ret.append([0,0,0,9000000,9000000,9000000,9000000,9000000,9000000,9000000,0,0,9000000,9000000,9000000,9000000])

    elif _map == 4:
        ret.append([9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066,9000066])
        ret.append([100,100,100,100,100,100,100,100,100,100,100,100,100,100])
        ret.append([100,100,100,100,100,100,100,100,9134100,9136100,100,100,100,100])
        ret.append([9000000,9000000,9000000,9000000,175100,100,100,100,135100,137100])
        ret.append([0,0,0,9000000,176100,100,100,100,9104100,9104100])
        ret.append([0,0,0,9000000,176100,100,100,96217100,9140100,9141100])
        ret.append([0,0,0,9000000,177100,100,100,100,142100,143100])
        ret.append([0,0,9000000,9000000,9000000,9000000,100,100,9000000,9000000,9000000])
        ret.append([0,0,0,0,0,9000000,107100,109100,9000000,0,0])
        ret.append([0,0,0,0,0,9000000,0,0,9000000,0,0])

    elif _map == 5:
        ret.append([9000000,0,0,9000000,9000000,9000000,9000000,9000000,0,9000000])
        ret.append([9000021,101,102,9000021,9000030,9042030,9000103,9000030,104,9000030])
        ret.append([100100,107100,109100,100,100,100,100,100,100,100])
        ret.append([9104100,9104100,100,100,100,100,100,100,158100,100])
        ret.append([101100,100,100,100,100,100,100,100,159100,160100])
        ret.append([100,100,100,100,100,100,100,100,100,100])

    return ret

#--------------------------------------------------
# Map Draw function
#--------------------------------------------------
def MapDraw(bg, x: int, y: int):
    x = x - 10
    y = y - 7
    selectIndex: int = 0

    # map draw
    bg.fill(idef.COLOR_BLACK)
    for j in range(15):
        if y + j < 0 or y + j >= len(mapNow):
           continue

        for i in range(21):
            if x + i < 0 or x + i >= len(mapNow[y+j]):
               continue

            selectIndex = mapNow[y+j][x+i]
            bg.blit(mapImg[selectIndex % MAP_IMG_ITEM], [32 * i - 16, 32 * j])
            selectIndex = int(selectIndex / MAP_IMG_ITEM)
            bg.blit(overMapImg[selectIndex % MAP_IMG_ITEM], [32 * i - 16, 32 * j])

    # character draw
    if charShowFlag == 1:
        bg.blit(charImg,[idef.WINDOW_WIDTH/2 - 16, idef.WINDOW_HEIGHT/2 - 16])

#--------------------------------------------------
# player direction image read function
#--------------------------------------------------
def CharDraw(bg, _dir: int):
    # enable change global value
    global dir
    global charImg
    global dirChar
    dirChar = _dir
    if _dir == DIR_L:
        if int(dir/10) == 0:
            dir = dir + 1
            if(dir >= 6):
                dir = 0
        else:
            dir = 0
        charImg = sideImg[dir]

    if _dir == DIR_R:
        if int(dir/10) == 1:
            dir = dir + 1
            if(dir >= 16):
                dir = 10
        else:
            dir = 10
        charImg = sideImg[5-dir+10]

    if _dir == DIR_D:
        if int(dir/10) == 2:
            dir = dir + 1
            if(dir >= 26):
                dir = 20
        else:
            dir = 20
        charImg = frontImg[dir-20]

    if _dir == DIR_U:
        if int(dir/10) == 3:
            dir = dir + 1
            if(dir >= 36):
                dir = 30
        else:
            dir = 30
        charImg = frontImg[5-dir+30]

#--------------------------------------------------
# Move check function
#--------------------------------------------------
def MoveCheck(x: int, y: int):
    if y < 0 or len(mapNow) <= y:
        return 1
    elif x < 0 or len(mapNow[y]) <= x:
        return 1
    elif int(mapNow[y][x] / (MAP_IMG_ITEM*MAP_IMG_ITEM)) == 0:
       return 0
    else:
       return 1

def SubCharShow(bg, num: int, _x: int, _y: int):
    x = 32 * _x - 16
    y = 32 * _y
    bg.blit(overMapImg[num],[x,y])

def TileDraw(bg, num: int, _x: int, _y: int):
    x = 32 * _x - 16
    y = 32 * _y
    bg.blit(mapImg[num],[x,y])


#--------------------------------------------------
# Map Main function
#--------------------------------------------------
def MapMain(bg, clk):
    # enable change global value
    global posX, posY
    global mapNow
    global mapNum
    global charShowFlag

    # local value
    timer: int = 0
    scene: int = 0
    walkTimer: int = 0
    walkFlag: int = 0
    key: int = 0
    keySelectFlag: int = 0
    pushSelect: int = 0
    pushCount: int = 0
    eventState: int = -1
    story: int = 0
    charShowFlag = 0        # 0:非表示 1:表示
    # font set
    messageFont = pygame.font.Font(idef.FONT_FILE_PATH, idef.MESSAGE_FONT_SIZE)
    
    # key input setup
    pygame.key.set_repeat(1,1)

    mapNum = 0
    mapNow = MapLoad(mapNum)
    
    user = idef.player()
    user.Name = "大腸菌"

    #-----------------------------------------------------------
    # story 
    #  0 : 黒い画面
    #  1 : 学生Aと博士の会話
    #  2 : O157を倒すまで
    #  3 : 黒い画面
    #  4 : ユーグレナ撃破　まで
    #  5 : 好熱菌を撃破まで
    #  6 : 粘菌撃破まで
    #  7 : 完全体157倒すまで
    #  8 : エンドまで
    #-----------------------------------------------------------

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

                # 連射後のご入力防止
                pygame.event.clear()

        # game state update
        bg.fill(idef.COLOR_WHITE)
        time = pygame.time.get_ticks()
        MapDraw(bg, posX, posY)

        # 連射防止
        if key & idef.KEY_SELECT == idef.KEY_SELECT and keySelectFlag == 0:
            keySelectFlag = 1
            pushSelect = 1
        elif key & idef.KEY_SELECT != idef.KEY_SELECT and keySelectFlag == 1:
            keySelectFlag = 0

        # no event
        if eventState == 0:
            # map移動実施
            if key & idef.KEY_MOVE > 0 and walkFlag == 0:
                walkFlag = 1
                walkTimer = time

                # 上キー入力
                if key & idef.KEY_UP == idef.KEY_UP:
                    if MoveCheck(posX, posY - 1) == 0:
                        posY = posY - 1
                    CharDraw(bg, DIR_U)

                # 下キー入力
                if key & idef.KEY_DOWN == idef.KEY_DOWN:
                    if MoveCheck(posX, posY + 1) == 0:
                        posY = posY + 1
                    CharDraw(bg, DIR_D)

                # 左キー入力
                if key & idef.KEY_LEFT == idef.KEY_LEFT:
                    if MoveCheck(posX - 1, posY) == 0:
                        posX = posX - 1
                    CharDraw(bg, DIR_L)
        
                # 右キー入力
                if key & idef.KEY_RIGHT == idef.KEY_RIGHT:
                    if MoveCheck(posX + 1, posY) == 0:
                        posX = posX + 1
                    CharDraw(bg, DIR_R)

                # 座標表示
                print(str(mapNum) + ", " + str(posX) + ", " + str(posY))
            
                # 座標イベント（マップ移動など）
                # ４号館2階
                if mapNum == 0:
                    if posX == 10 and posY == 12 and story >= 4:
                        mapNum = 2
                        posX = 2
                        posY = 2
                        mapNow = MapLoad(mapNum) 
                
                    elif posX == 11 and posY == 12 and story >= 4:
                        mapNum = 2
                        posX = 3
                        posY = 2
                        mapNow = MapLoad(mapNum)   

                    if posX == 0 and posY == 2:
                        eventState = 950

                # 外
                elif mapNum == 1:
                    if 2 <= posX and posX <= 5 and 6 <= posY and posY <= 9 and story == 4:
                        eventState = -1

                    if posX == 18 and posY == 7:
                        mapNum = 2
                        posX = 2
                        posY = 6
                        mapNow = MapLoad(mapNum) 
                
                    if posX == 18 and posY == 8:
                        mapNum = 2
                        posX = 3
                        posY = 6
                        mapNow = MapLoad(mapNum)   
                    
                    if posX == 31 and posY == 14:
                        mapNum = 3
                        posX = 10
                        posY = 17
                        mapNow = MapLoad(mapNum) 
                
                    if posX == 32 and posY == 14:
                        mapNum = 3
                        posX = 11
                        posY = 17
                        mapNow = MapLoad(mapNum) 

                    if posX == 35 and posY == 26:
                        mapNum = 4
                        posX = 7
                        posY = 8
                        mapNow = MapLoad(mapNum) 
                    
                    if posX == 22 and posY == 26 and story >= 7:
                        mapNum = 5
                        posX = 2
                        posY = 2
                        mapNow = MapLoad(mapNum) 

                    if posX == 23 and posY == 17:
                        mapNum = 5
                        posX = 8
                        posY = 3
                        mapNow = MapLoad(mapNum) 

                # 4号館1階
                elif mapNum == 2:
                    if posX == 2 and posY == 7:
                        mapNum = 1
                        posX = 17
                        posY = 7
                        mapNow = MapLoad(mapNum) 
                
                    if posX == 3 and posY == 7:
                        mapNum = 1
                        posX = 17
                        posY = 8
                        mapNow = MapLoad(mapNum) 

                    if posX == 2 and posY == 1:
                        mapNum = 0
                        posX = 10
                        posY = 11
                        mapNow = MapLoad(mapNum) 

                    if posX == 3 and posY == 1:
                        mapNum = 0
                        posX = 11
                        posY = 11
                        mapNow = MapLoad(mapNum) 

                # 図書館
                elif mapNum == 3:
                    if posX == 6 and 11 <= posY and posY <= 12 and story == 6:
                        eventState = -1

                    if posX == 11 and posY == 18:
                        mapNum = 1
                        posX = 32
                        posY = 15
                        mapNow = MapLoad(mapNum) 
                
                    if posX == 10 and posY == 18:
                        mapNum = 1
                        posX = 31
                        posY = 15
                        mapNow = MapLoad(mapNum) 

                # 2号館
                elif mapNum == 4:
                    if 6 <= posX and posX <= 7 and posY == 7 and story == 5:
                        eventState = -1

                    if posX == 7 and posY == 9:
                        mapNum = 1
                        posX = 35
                        posY = 27
                        mapNow = MapLoad(mapNum) 

                    if posX == 6 and posY == 9:
                        mapNum = 1
                        posX = 35
                        posY = 27
                        mapNow = MapLoad(mapNum) 

                # 総合研究棟
                elif mapNum == 5:
                    if posX == 2 and posY == 0:
                        mapNum = 1
                        posX = 22
                        posY = 27
                        mapNow = MapLoad(mapNum) 
            
                    if posX == 1 and posY == 0:
                        mapNum = 1
                        posX = 22
                        posY = 27
                        mapNow = MapLoad(mapNum) 

                    if posX == 8 and posY == 0:
                        mapNum = 1
                        posX = 23
                        posY = 19
                        mapNow = MapLoad(mapNum) 
                        if story == 7:
                            eventState = -1
                        
            elif walkFlag == 1:
                # 移動速度調整
                if time - walkTimer >= 50:
                    walkFlag = 0
            else:
                walkFlag = 0
                walkTimer = time

            # 決定キー入力
            if pushSelect == 1:
                pushSelect = 0
                print("select push")
                _x: int = 0
                _y: int  = 0
                if dirChar == DIR_D and posY < len(mapNow) - 1: _y = 1
                elif dirChar == DIR_U and posY > 0: _y = -1
                elif dirChar == DIR_L and posX > 0: _x = -1
                elif dirChar == DIR_R and posX < len(mapNow[posY]) - 1: _x = 1
                event = int(mapNow[posY + _y][posX + _x] / (MAP_IMG_ITEM*MAP_IMG_ITEM))
                    
                # 学生Aイベント
                if event == 1:
                    eventState = 100

                # 学生Bイベント
                elif event == 2:
                    eventState = 200

                # 博士イベント
                elif event == 3:
                    eventState = 300

                # 看板イベント
                elif event == 4:
                    eventState = 400

                # 貼り紙イベント
                elif event == 5:
                    eventState = 500

                elif event == 6:
                    eventState = 600

                elif event == 7:
                    eventState = 700

                elif event == 8:
                    eventState = 800

                elif event == 10:
                    eventState = 1000

                elif event == 51:
                    eventState = 510

                elif event == 52:
                    eventState = 520

                elif event == 53:
                    eventState = 530

                elif event == 54:
                    eventState = 540
   
                elif event == 55:
                    eventState = 550

                elif event == 56:
                    eventState = 560

                elif event == 57:
                    eventState = 570

                elif event == 58:
                    eventState = 580

                elif event == 71:
                    eventState = 710

                elif event == 72:
                    eventState = 720

                elif event == 73:
                    eventState = 730

                elif event == 74:
                    eventState = 740
   
                elif event == 75:
                    eventState = 750

                elif event == 76:
                    eventState = 760

                elif event == 77:
                    eventState = 770

                elif event == 81:
                    eventState = 810

                elif event == 82:
                    eventState = 820

                elif event == 90:
                    eventState = 900

                elif event == 91:
                    eventState = 910

                elif event == 92:
                    eventState = 920

                elif event == 93:
                    eventState = 930

                elif event == 94:
                    eventState = 940

                elif event == 96:
                    eventState = 960


        # select 入力待ち
        elif eventState == 1:
            idef.MessageDraw(bg,messageFont)
            if pushSelect == 1:
                pushSelect = 0
                eventState = 0

        elif eventState == -1:
            if story == 0:
                bg.fill(idef.COLOR_BLACK)
                if pushCount == 0:
                    pushCount = pushCount + 1
                    idef.MessageInit()
                    idef.MessageSet("剣と魔法のファンタジーの世界。");
                    idef.MessageSet("そんな世界で、理工学を研究する者共が集う場所……")
                    idef.MessageSet("グンマー国のとある大学。")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        idef.MessageInit()
                        idef.MessageSet(" ")
                        idef.MessageSet("すべてはここから始まる。")
                        pushCount = 2
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushCount = 0
                        pushSelect = 0
                        story = 1
                        posX = 11
                        posY = 3
            elif story == 1:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("学生A「ゲホッゲホッ、やってしまった…。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("教授「すごい音が聞こえたが…君、大丈夫か！？」")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageInit()
                        idef.MessageSet("学生A「大丈夫です！」")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageInit()
                        idef.MessageSet("教授「返事ができるなら大丈夫そうだな。」")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageInit()
                        idef.MessageSet("学生A「あの、僕何も言ってないですよ。」")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageInit()
                        idef.MessageSet("教授「えっ？」")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        timer = 0
                elif pushCount == 7:
                    timer = timer + 1
                    if int(timer) % 2 == 0:
                        charShowFlag = 1
                    else:
                        charShowFlag = 0
                    if timer >= 50:
                        pushSelect = 0
                        pushCount = 8
                        timer = 0
                        charShowFlag = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「これは……大腸菌だ。それもとても大きな。」")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("教授「オートクレーブしようにも、")
                        idef.MessageSet("　　　大きすぎて装置に入りそうもない。")
                        idef.MessageSet("　　　どうしたものか。」")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 10
                        idef.MessageInit()
                        idef.MessageSet("説明しよう！オートクレーブとは、")
                        idef.MessageSet("高温・高圧の蒸気で菌を退治する処理である！")
                elif pushCount == 10:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 11
                        idef.MessageInit()
                        idef.MessageSet("？？？「うわぁぁーーーっ！？」")
                elif pushCount == 11:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 12
                        idef.MessageInit()
                        idef.MessageSet("学生A「この声は……隣の実験室からだ！」")
                elif pushCount == 12:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
                        story = 2
            elif story == 2:
                if pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("？？？「オレは，O157．")
                        idef.MessageSet("　　　　食中毒の原因となる菌だぜ」")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 11
                        idef.MessageInit()
                        idef.MessageSet("O157「オレ様が最強の菌だということを、")
                        idef.MessageSet("　　　まずはこの大学で暴れてやる！」")
                        idef.MessageSet("　　　世界中に知らしめてやるぜ！")
                elif pushCount == 11:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 12
                elif pushCount == 12:
                    ibattle.BattleMain(bg,clk,user, 1)
                    pushCount =13
                    idef.MessageInit()
                    idef.MessageSet("O157「くっそ～、覚えてろよ！」")
                elif pushCount == 13:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 14
                        idef.MessageInit()
                        idef.MessageSet("教授「さっきの大腸菌が、アレを『処理』してくれたのか…？」")
                elif pushCount == 14:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 15
                        idef.MessageInit()
                        idef.MessageSet("学生A「Bさん、外でなにがあったんだい？」")
                elif pushCount == 15:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 16
                        idef.MessageInit()
                        idef.MessageSet("学生B「さっき大きな音がした後、")
                        idef.MessageSet("　　　　おかしなサイズの菌が四号館から出てきたです。」")
                elif pushCount == 16:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 17
                        idef.MessageInit()
                        idef.MessageSet("教授「巨大な菌は他にもいるのか。")
                        idef.MessageSet("　　　オートクレーブが使えないとなると……」")
                elif pushCount == 17:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 18
                        idef.MessageInit()
                        idef.MessageSet(user.Name + "「まかせて！」")
                elif pushCount == 18:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 19
                        idef.MessageInit()
                        idef.MessageSet("学生A「ありがとう！それじゃ、君に資料を渡そう。")
                        idef.MessageSet("　　　　何か困ったことがあったら、僕にきくように。")
                elif pushCount == 19:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 20
                        idef.MessageInit()
                        idef.MessageSet(user.Name + "「わかった！」")
                elif pushCount == 20:
                    SubCharShow(bg, 1, 8, 10)
                    SubCharShow(bg, 3, 9, 10)
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = -1
                        story = 3
            elif story == 3:
                bg.fill(idef.COLOR_BLACK)
                if pushCount == 0:
                    pushCount = pushCount + 1
                    idef.MessageInit()
                    idef.MessageSet("かくして、大腸菌の冒険が幕を開けた。");
                    idef.MessageSet(user.Name + "は、無事キャンパスの平和を")
                    idef.MessageSet("取り戻すことができるのだろうか？")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushCount = 0
                        pushSelect = 0
                        eventState = 0
                        posX = 11
                        posY = 3
                        dir = 0
                        story = 4
            elif story == 4:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("？？？「誰？…なんだ、君も菌か。」")
                    idef.MessageSet("　　　　最近、栄養素がどうとかいう理由で、")
                    idef.MessageSet("　　　　人間に命を狙われているんだよ……」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("ユーグレナ「ボクはユーグレナ。")
                        idef.MessageSet("　　　　　　人間にはミドリムシって呼ばれてるよ。」")
                        idef.MessageSet("　　　　　　今まで見向きもされなかったのに、")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　　　　いきなりチヤホヤされ出したと思ったら")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　　　　これさ！")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageSet("　　　　　　こんなところで死んでたまるか！")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageSet("　　　　　　人間に手を貸すなら、")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        idef.MessageSet("　　　　　　同じ菌だろうと容赦しないよ！")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        ibattle.BattleMain(bg,clk,user, 2)
                        user.Command.append("プラスミド[ユーグレナ]")
                        pushCount = 8
                        idef.MessageInit()
                        idef.MessageSet("ユーグレナ「そうか、これもまた運命……")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("［学生証の破片1を拾った］")
                        idef.MessageSet("《研究室に戻って、報告しよう》")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        story = 5
                        eventState = 0
            elif story == 5:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("？？？「おいおい、邪魔しないでくれよ。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("好熱菌「おいらは好熱菌。")
                        idef.MessageSet("　　　　とにかくあったか～～い場所が大好きなのさ！")
                        idef.MessageSet("　　　　今ちょうどいい場所を見つけたところなんだ。")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　　でも……奪おうってんなら、")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　　話は別さ。かかってきな！")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        ibattle.BattleMain(bg,clk,user, 3)
                        user.Command.append("プラスミド[好熱菌]")
                        pushCount = 8
                        idef.MessageInit()
                        idef.MessageSet("好熱菌「ぐう、熱さが足りない！」")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("［学生証の破片2を拾った］")
                        idef.MessageSet("《研究室に戻って、報告しよう》")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        story = 6
                        eventState = 0
            elif story == 6:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("？？？「あら？あなたは……大腸菌ね。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("粘菌「アタシは粘菌。")
                        idef.MessageSet("　　　変形菌とも呼ばれているわ。")
                        idef.MessageSet("　　　キノコやアメーバも私のお友達よ。")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　人間にも、私の美しさは伝わっているわ。")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　写真集だって何冊もあるのよ！")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageSet("　　　それなのに、")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageSet("　　　研究者達は“粘菌コンピュータ”の研究ばかり。")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = -7
                        idef.MessageSet("　　　ホント、嫌になっちゃうわ。")
                elif pushCount == -7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        idef.MessageSet("　　　もう窮屈な思いはこりごりよ！」")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        ibattle.BattleMain(bg,clk,user, 4)
                        user.Command.append("プラスミド[粘菌]")
                        pushCount = 8
                        idef.MessageInit()
                        idef.MessageSet("粘菌「美しさだけではダメなのね……！」")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("［学生証の破片3を拾った］")
                        idef.MessageSet("《研究室に戻って、報告しよう》")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        story = 7
                        eventState = 0
            elif story == 7:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("？？？「待っていたぜ、大腸菌！」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageInit()
                        idef.MessageSet("？？？「待っていたぜ、大腸菌！")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageInit()
                        idef.MessageSet("　　　　研究室のヤツらを返して欲しくば、")
                        idef.MessageSet("　　　　オレ様と勝負するんだな。」")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageInit()
                        idef.MessageSet("O157「忘れたとは言わせねえ、")
                        idef.MessageSet("　　　オレだよ！O157様だ！")
                        idef.MessageSet("　　　あの時倒したはずだって？")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageSet("　　　残念だったなぁ、プラスミドだよ！！")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageInit()
                        idef.MessageSet("説明しよう！プラスミドとは、")
                        idef.MessageSet("遺伝子組換え実験で利用される")
                        idef.MessageSet("『遺伝子の運び手』である！")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = -7
                        idef.MessageInit()
                        idef.MessageSet("プラスミドの持つ遺伝子は、")
                        idef.MessageSet("菌に様々な能力を与えるぞ。")
                        idef.MessageSet("『遺伝子の運び手』である！")
                elif pushCount == -7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = -8
                        idef.MessageInit()
                        idef.MessageSet("ちなみに、")
                        idef.MessageSet("薬の効かない菌が生まれるのも")
                        idef.MessageSet("このプラスミドのせいなのだ！")
                elif pushCount == -8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        idef.MessageInit()
                        idef.MessageSet("O157「キャンパス中のプラスミドを集め、")
                        idef.MessageSet("　　　オレ様は完全体となった！")
                        idef.MessageSet("　　　あの時の恨み、ここで晴らしてやるぜ！")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        ibattle.BattleMain(bg,clk,user, 5)
                        pushCount = 8
                        idef.MessageInit()
                        idef.MessageSet("O157「そんなバカな、オレは最強の力を手に入れたんだぞ！」")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("《研究室に戻ろう》")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        story = 8
                        eventState = 0
            elif story == 8:
                if pushCount == 0:
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("教授「O157に勝てたのは")
                    idef.MessageSet("　　　キャンパス中のプラスミドを集め、")
                    idef.MessageSet("　　　O157が弱体化したからだ")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　プラスミドはお前たち菌に恩恵を")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　与えてくれるものばかりではないのだよ！")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　さて、"+user.Name + "くん")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageSet("　　　これまでの活躍、大変ご苦労だった。")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageSet("　　　研究室でゆっくり休んでくれたまえ……")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        idef.MessageSet("　　　と言いたいところだが、")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 8
                        idef.MessageSet("　　　君にはオートクレーブを受けてもらう！")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 8
                        idef.MessageSet("　　　研究室から菌を流出させてはいけないのだ！")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageInit()
                        idef.MessageSet("《説明しよう！")
                        idef.MessageSet("遺伝子組み換えをした生きた菌の、")
                        idef.MessageSet("実験室の外への持ち出しは")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 10
                        idef.MessageSet("『カルタヘナ条約』で")
                elif pushCount == 10:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 11
                        idef.MessageSet("禁止されているんだ！》")
                elif pushCount == 11:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 12
                        timer = 0
                elif pushCount == 12:
                    bg.fill(idef.COLOR_BLACK)
                    timer = timer + 1
                    if timer >= 10:
                        timer = 0
                        posX = 25
                        posY = 1
                        pushCount = 13
                        pushSelect = 0
                        idef.MessageInit()
                        idef.MessageSet("学生B「教授！" + user.Name + "さんは、")
                        idef.MessageSet("　　　命の恩人なのです！")
                        idef.MessageSet("　　　オートクレーブなんて、駄目で～す！")
                elif pushCount == 13:
                    idef.MessageDraw(bg, messageFont)
                    SubCharShow(bg, 3, 12,8)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 14
                        idef.MessageInit()
                        idef.MessageSet("教授「問答無用！菌は死すべし！」")
                elif pushCount == 14:
                    idef.MessageDraw(bg, messageFont)
                    SubCharShow(bg, 3, 12,8)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 15
                        idef.MessageInit()
                        idef.MessageSet(user.Name + "「話が違うよ！」")
                elif pushCount == 15:
                    idef.MessageDraw(bg, messageFont)
                    SubCharShow(bg, 3, 12,8)
                    timer = timer + 1
                    if int(timer) % 2 == 0:
                        charShowFlag = 1
                    else:
                        charShowFlag = 0
                    if timer >= 50:
                        pushSelect = 0
                        pushCount = 16
                        timer = 0
                        charShowFlag = 0
                elif pushCount == 16:
                    timer = timer + 1
                    SubCharShow(bg, 3, 12,8)
                    if timer >= 20:
                        timer = 0
                        posX = 11
                        posY = 3
                        pushCount = 17
                        pushSelect = 0
                        idef.MessageInit()
                        idef.MessageSet("学生A「……。」")
                        idef.MessageSet("　　　いやー、大変な一日だったな。")
                        idef.MessageSet("　　　教授、僕が装置を壊したこと忘れてるみたいだけど……")
                    if timer >= 10:                
                        bg.fill(idef.COLOR_BLACK)
                elif pushCount == 17:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 18
                        idef.MessageSet("　　　まあいっか！」")
                elif pushCount == 18:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 19
                        idef.MessageInit()
                        idef.MessageSet("かくして、キャンパスに再び平和が訪れた。")
                        idef.MessageSet("大腸菌が一匹うろついているけど…、")
                        idef.MessageSet("これも誤差の範囲内だね！")
                elif pushCount == 19:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 19
                        iroll.StaffrollMain(bg, clk)

        # 学生A map 0
        elif eventState == 100:
            if story == 2:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「この声は……廊下からだ！」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 4:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「外から来たBさんなら、")
                        idef.MessageSet("　　　逃げ出したサンプルについて、")
                        idef.MessageSet("　　　何か分かるかもしれないね。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 5:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「" + user.Name + "か．")
                        idef.MessageSet("　　　Bさんが、")
                        idef.MessageSet("　　　次の場所への手がかりを手に入れたみたいだよ。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 6:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「さすが" + user.Name)
                        idef.MessageSet("　　　仕事が早いね。")
                        idef.MessageSet("　　　Bさんが君を探していたよ。」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 7:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("返事がない...")
                        idef.MessageSet("生気を感じられない...")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 8:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生A「よう！" + user.Name + "さん")
                        idef.MessageSet("　　　　教授にはなしかけてください！")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0

        # 学生B map 0
        elif eventState == 200:
            if story == 2:
                if pushCount == 0:
                    pushSelect = 0
                    pushCount = 1
                    eventState = -1
                    idef.MessageInit()
                    idef.MessageSet("学生B「た、助けてくださ～い！」")
            elif story == 4:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生B「私、先輩達が心配で心配で、")
                        idef.MessageSet("　　　急いで研究室へ向かったです！")
                        idef.MessageSet("　　　出会った菌？")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　お清めの塩を撒いて退治したです！")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　そういえば池の近くで、")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　何やら不審な影を発見したです！")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0   
            elif story == 5:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生B「機械科の学生さんが、")
                        idef.MessageSet("　　　二号館で怪しい影を見たらしいです！")
                        idef.MessageSet("　　　今日は休みなのに、なんで機械科がいるんでしょう？")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　不思議です～。」")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 6:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生B「" + user.Name + "さん")
                        idef.MessageSet("　　　図書館で不気味な音がするそうです！")
                        idef.MessageSet("　　　怖いので調べてきてください～！")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 7:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生B「よかった！" + user.Name + "さん")
                        idef.MessageSet("　　　戻ったんですね！")
                        idef.MessageSet("　　　聞いてください！")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　先輩達が、")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　謎の影に生気を吸われたんです！")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 4
                        idef.MessageSet("　　　お願いです、")
                elif pushCount == 4:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 5
                        idef.MessageSet("　　　先輩達を助けてください～！")
                elif pushCount == 5:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 6
                        idef.MessageSet("　　　集めた学生証を使えば、")
                elif pushCount == 6:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 7
                        idef.MessageSet("　　　総研棟に入れるです！")
                elif pushCount == 7:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 8
                        idef.MessageSet("　　　私は盛り塩のおかげで大丈夫だったです")
                elif pushCount == 8:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 9
                        idef.MessageSet("　　　早く先輩達を助けに行くです！")
                elif pushCount == 9:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 8:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("学生B「よかった！" + user.Name + "さん")
                        idef.MessageSet("　　　　教授にはなしかけてください！")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0

        # 博士 map 0
        elif eventState == 300:
            if story == 2:
                if pushCount == 0:
                    pushSelect = 0
                    pushCount = 1
                    idef.MessageInit()
                    idef.MessageSet("教授「今の声はなんだ」")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 4:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("教授「私の研究室では、")
                        idef.MessageSet("　　　主に菌や微生物の研究をしている。")
                        idef.MessageSet("　　　爆発で壊れた装置には、")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　君を含めて『5種類のサンプル』が")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 3
                        idef.MessageSet("　　　入っていたのだが…")
                elif pushCount == 3:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0  
            elif story == 5:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("教授「君のおかげで、")
                        idef.MessageSet("　　　見つけていないサンプルはあと2つだ。")
                        idef.MessageSet("　　　この調子で頼むぞ。")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 2
                        idef.MessageSet("　　　…新しいオートクレーブ装置が必要だな。")
                elif pushCount == 2:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0 
            elif story == 6:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("教授「ちょうど休みで人が居ないから、")
                        idef.MessageSet("　　　大腸菌が出歩いていても問題ないな。")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 7:
                if pushCount == 0:
                        pushSelect = 0
                        pushCount = 1
                        idef.MessageInit()
                        idef.MessageSet("返事がない...")
                        idef.MessageSet("生気を感じられない...")
                elif pushCount == 1:
                    idef.MessageDraw(bg, messageFont)
                    if pushSelect == 1:
                        pushSelect = 0
                        pushCount = 0
                        eventState = 0
            elif story == 8:
                if pushCount == 0:
                    pushSelect = 0
                    pushCount = 0
                    eventState = -1

        # 看板 map 3
        elif eventState == 400:
            idef.MessageInit()
            idef.MessageSet("「このさき改装中、通れません。」");
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # 貼り紙 map 0
        elif eventState == 500:
            idef.MessageInit()
            idef.MessageSet("「実験器具　は　やさしく　あつかおう」");
            idef.MessageSet("　とかいてある。")
            eventState = 1

        # 机の花瓶 map 0
        elif eventState == 510:
            idef.MessageInit()
            idef.MessageSet("ビリビリに　やぶれた　ろんぶん　が");
            idef.MessageSet("かびんの　したじき　に　なっている。")
            idef.MessageSet("「リジェクト」　と　かいてある　けど")
            eventState = 511
        elif eventState == 511:
            idef.MessageDraw(bg, messageFont)
            if pushSelect == 1:
                pushSelect = 0
                idef.MessageSet("どういう　いみ　だろう　・・・？")
                eventState = 1

        # 壁のメモ map 0
        elif eventState == 520:
            idef.MessageInit()
            idef.MessageSet("「９時　から　１７時　は　コアタイム」");
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # 4号館真ん中机みぎ map 0
        elif eventState == 530:
            idef.MessageInit()
            idef.MessageSet("「博士　に　進む　か　まようなあ......。」");
            idef.MessageSet("　と　かいてある。")
            idef.MessageSet("　どうして　まよって　いるんだろう　・・・？")
            eventState = 1

        # 4号館真ん中机ひだり map 0
        elif eventState == 540:
            idef.MessageInit()
            idef.MessageSet("じっけんノート　が　ある。");
            idef.MessageSet("・PCR　する")
            idef.MessageSet("・アガロースゲル　電気泳動")
            eventState = 541
        elif eventState == 541:
            idef.MessageDraw(bg, messageFont)
            if pushSelect == 1:
                pushSelect = 0
                idef.MessageSet("・ゲル抽出")
                idef.MessageSet("・・・・・・")
                idef.MessageSet("　むずかしくて　なんのことか　さっぱり　わからないや。")
                eventState = 1

         # 4号館左部屋机みぎ map 0
        elif eventState == 550:
            idef.MessageInit()
            idef.MessageSet("「やりたい　研究　アイデア」");
            idef.MessageSet("　と　かいてある。")
            idef.MessageSet("　きたない　じ　で　びっしりと")
            eventState = 551
        elif eventState == 551:
            idef.MessageDraw(bg, messageFont)
            if pushSelect == 1:
                pushSelect = 0
                idef.MessageSet("　かいてあって　よめない......。")
                eventState = 1
            
        # 4号館左部屋机ひだり map 0
        elif eventState == 560:
            idef.MessageInit()
            idef.MessageSet("じっけんノート　だ。");
            idef.MessageSet("「３７ ℃ 培養　１６時間」")
            idef.MessageSet("「ミス：アンピシリン　を　入れわすれた」")
            eventState = 561
        elif eventState == 561:
            idef.MessageDraw(bg, messageFont)
            if pushSelect == 1:
                pushSelect = 0
                idef.MessageSet("と　かいてある。")
                idef.MessageSet("アンピシリン　って　なんだろう......。")
                idef.MessageSet("なんとなく　いやな　ひびき　だなあ。")
                eventState = 1

        # 4号館左部屋　貼り紙 map 0
        elif eventState == 570:
            idef.MessageInit()
            idef.MessageSet("「よい　研究　を　するには");
            idef.MessageSet("　やっぱり　睡眠　が　たいせつ」")
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # 4号館左部屋　黒い額縁 map 0
        elif eventState == 580:
            idef.MessageInit()
            idef.MessageSet("ふせん　が　ぺたぺた　貼ってある。");
            idef.MessageSet("ちしき　は　たましい　の　食べ物。") 
            idef.MessageSet("と　かいてある。")
            eventState = 581
        elif eventState == 581:
            idef.MessageDraw(bg, messageFont)
            if pushSelect == 1:
                pushSelect = 0
                idef.MessageSet("たましいって何だろう……？")
                idef.MessageSet("ぼくにも　あるのかな。")
                eventState = 1

         # オートクレーブ map 0
        elif eventState == 600:
            idef.MessageInit()
            idef.MessageSet("オートクレーブ　だ......。");
            idef.MessageSet("もう　あっちへ　いこう。")
            eventState = 1

        # map 0
        elif eventState == 700:
            idef.MessageInit()
            idef.MessageSet("「７０％　エタノール」");
            idef.MessageSet("と　かいてある。")
            idef.MessageSet("なんだか　いやな　かんじが　する。")
            eventState = 1

        # バケツ map 0
        elif eventState == 710:
            idef.MessageInit()
            idef.MessageSet("これは......　えんそ　の　においが　する。");
            idef.MessageSet("なんだか　ちかよりたくない。")
            eventState = 1

        # 顕微鏡　map 0
        elif eventState == 720:
            idef.MessageInit()
            idef.MessageSet("けんびきょう　が　ある。");
            eventState = 1

        # メスシリンダー map 0
        elif eventState == 730:
            idef.MessageInit()
            idef.MessageSet("メスシリンダー　と");
            idef.MessageSet("アルコールランプ　が　ある。")
            eventState = 1

        # LB培地 map 0
        elif eventState == 740:
            idef.MessageInit()
            idef.MessageSet("「LB培地」　と　かいてある。");
            idef.MessageSet("　おいしそうな　においが　する......。")
            eventState = 1

        # 論文 map 0
        elif eventState == 750:
            idef.MessageInit()
            idef.MessageSet("いろいろな　ろんぶん　が　おいてある。");
            eventState = 1

        # 冷蔵庫うえ map 0
        elif eventState == 760:
            idef.MessageInit()
            idef.MessageSet("「冷蔵庫　の　ドア　は");
            idef.MessageSet("　こまめに　しめよう　！！！」")
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # 冷蔵庫した map 0
        elif eventState == 770:
            idef.MessageInit()
            idef.MessageSet("「さがしもの　は");
            idef.MessageSet("　ドア　を　閉めてから　ゆっくり」")
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # なし
        elif eventState == 800:
            idef.MessageInit()
            idef.MessageSet("おや　かわいい");
            idef.MessageSet("　あひるが　ある。")
            eventState = 1

        # map1
        elif eventState == 810:
            idef.MessageInit()
            idef.MessageSet("・・・・・・");
            idef.MessageSet("へんてこりんな　せきぞう　が　ある。")
            eventState = 1

        # map1
        elif eventState == 820:
            idef.MessageInit()
            idef.MessageSet("ここは　機械科の　城");
            eventState = 1

        # map 3　掲示板
        elif eventState == 900:
            idef.MessageInit()
            idef.MessageSet("「本の返却期限が過ぎている方は");
            idef.MessageSet("至急、返却してください」")
            idef.MessageSet("　と　かいてある。")
            eventState = 1

        # map 3　本棚うえ左
        elif eventState == 910:
            idef.MessageInit()
            idef.MessageSet("にんげん　が　えいご　の　べんきょう　に");
            idef.MessageSet("つかう　ほん　が　たくさん　ある。")
            eventState = 1

        # map 3　本棚うえ右
        elif eventState == 920:
            idef.MessageInit()
            idef.MessageSet("にんげん　が　にほんご　の　べんきょう　に");
            idef.MessageSet("つかう　ほん　が　たくさん　ある。")
            eventState = 1

        # map 3　本棚した左
        elif eventState == 930:
            idef.MessageInit()
            idef.MessageSet("どこかで　きいたことの　ある　タイトルの");
            idef.MessageSet("ざっし　が　たくさん　おいてある。")
            eventState = 1

         # map 3　コピー機
        elif eventState == 940:
            idef.MessageInit()
            idef.MessageSet("「コピー　いちまい　１０円」");
            idef.MessageSet("　と　かいてある。")
            idef.MessageSet("　・・・そういえば　ぼくは　なぜ　じ　が　よめるんだろう。")
            eventState = 1

        elif eventState == 950:
            idef.MessageInit()
            idef.MessageSet("ゆっくり　休もう");
            idef.MessageSet("HP　と　MP　が　回復した")
            idef.MessageSet("")
            user.HP = user.MaxHP
            user.MP = user.MaxMP
            eventState = 1

        # map4  ミヤウチ
        elif eventState == 960:
            idef.MessageInit()
            idef.MessageSet("・・・・・・");
            idef.MessageSet("ミヤウチ「なんだよ　おれは　忙しいんだ」")
            idef.MessageSet("ミヤウチ「論文を　出したばかりなんだぞ」")
            eventState = 1

        # map 5
        elif eventState == 1000:
            idef.MessageInit()
            idef.MessageSet("「清掃中・立ち入り禁止」");
            idef.MessageSet("とかいてある。")
            eventState = 1

        pygame.display.update()
        clk.tick(33)

#----------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------
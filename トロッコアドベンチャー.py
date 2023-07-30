import pygame
from pygame.locals import *
import sys
import cv2
import numpy as np
import time
from pygame import mouse
import os
import random
SCREEN=Rect((0,0,1366,768))

class Bg_taiki:
    #ロゴ的なものを入れるか洞窟をそのまま写すか
    def __init__(self):
        self.bg_taiki_img=pygame.image.load("トロッコスタート待機画面（仮）2.png")
        self.bg_taiki_img=pygame.transform.scale(self.bg_taiki_img,(1366,768))
    def update(self):
        pass
    def draw(self,screen):
        screen.blit(self.bg_taiki_img,SCREEN)
class One:
    def __init__(self):
        self.img=pygame.image.load("onetest.png")
        self.img=pygame.transform.scale(self.img,(54,54))
    def update(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def draw(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def undraw(self):
        pass
        #あとで消す処理をする
class Two:
    def __init__(self):
        self.img=pygame.image.load("twotest.png")
        self.img=pygame.transform.scale(self.img,(54,54))
    def update(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def draw(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def undraw(self):
        pass
class Three:
    def __init__(self):
        self.img=pygame.image.load("threetest.png")
        self.img=pygame.transform.scale(self.img,(54,54))
    def update(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def draw(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def undraw(self):
        pass
class Four:
    def __init__(self):
        self.img=pygame.image.load("fourtest.png")
        self.img=pygame.transform.scale(self.img,(54,54))
    def update(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def draw(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def undraw(self):
        pass
class Five:
    def __init__(self):
        self.img=pygame.image.load("fivetest.png")
        self.img=pygame.transform.scale(self.img,(54,54))
    def update(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def draw(self,screen):
        screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//6))
    def undraw(self):
        pass

class Background_q_1:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testfile.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_1_True:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
#コピペ前に微調整する
class A_1_True:
    def __init__(self):
        self.img=pygame.image.load("problems/q_1/True_img.JPG")
        self.img=pygame.transform.scale(self.img,(162,162))
        self.basho=random.randint(0,1)

    def checkbasho(self):
        return self.basho    
    def update(self,screen):
        if self.basho==1:
            screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//2))
        else:
            #あとでleftをSCREENのRectから割算して取得するようにする
            screen.blit(self.img,(0,SCREEN.bottom//2))
class A_1_False:
    def __init__(self):
        self.img=pygame.image.load("problems/q_1/False_img.JPG")
        self.img=pygame.transform.scale(self.img,(162,162))
    def checkbasho(self,basho):
        if basho==1:
            self.basho=0
        if basho==0:
            self.basho=1

        
    def update(self,screen):
        if self.basho==1:
            screen.blit(self.img,(SCREEN.right//2,SCREEN.bottom//2))
        else:
            #あとでleftをSCREENのRectから割算して取得するようにする
            screen.blit(self.img,(0,SCREEN.bottom//2))
class Background_a_1_False:
    #落ちる
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_q_2:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testfile.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_2_True:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_2_False:
    #落ちる
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_q_3:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testfile.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_3_True:
    #ピンポン音、走る、この辺りでだまし映像を入れてもいいかも
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_3_False:
    #落ちる
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_q_4:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testfile.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_4_True:
    #走る
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_4_False:
    #落ちる映像
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_q_5:
    #走るトロッコ
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testfile.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_5_True:
    #ゴール演出
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))
class Background_a_5_False:
    #落ちる映像
    
    def __init__(self):
        self.backgraund_img = cv2.VideoCapture("testanswer.mp4")

    def update(self,screen):
        self.ret, self.frame = self.backgraund_img.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.frame = cv2.resize(self.frame,(1366,768))
        self.frame = cv2.flip(self.frame,1)
        self.frame = np.rot90(self.frame)
        self.frame = pygame.surfarray.make_surface(self.frame)
        screen.blit(self.frame, (0,0))
    
    def draw(self,screen):
        screen.blit(self.frame, (0,0))

def main():
    #初期設定
    pygame.init()
    screen=pygame.display.set_mode(SCREEN.size,FULLSCREEN)
    pygame.display.set_caption("Hello World")
    pygame.mouse.set_visible(False)
    clock=pygame.time.Clock()

    #登場する人・物・背景の作成
    bg_taiki=Bg_taiki()
    bg_img_q_1=Background_q_1()
    bg_img_a_1_True=Background_a_1_True()
    bg_img_a_1_False=Background_a_1_False()
    bg_img_q_2=Background_q_2()
    bg_img_a_2_True=Background_a_2_True()
    bg_img_a_2_False=Background_a_2_False()
    bg_img_q_3=Background_q_3()
    bg_img_a_3_True=Background_a_3_True()
    bg_img_a_3_False=Background_a_3_False()
    bg_img_q_3=Background_q_3()
    bg_img_a_3_True=Background_a_3_True()
    bg_img_a_3_False=Background_a_3_False()
    bg_img_q_4=Background_q_4()
    bg_img_a_4_True=Background_a_4_True()
    bg_img_a_4_False=Background_a_4_False()
    bg_img_q_5=Background_q_5()
    bg_img_a_5_True=Background_a_5_True()
    bg_img_a_5_False=Background_a_5_False()
    a_1_True=A_1_True()
    a_1_false=A_1_False()
    a_1_false.checkbasho(a_1_True.checkbasho())
    one=One()
    two=Two()
    three=Three()
    four=Four()
    five=Five()
    po=0
    #スタート待機画面
    while True:
        #画面をクリア
        screen.fill((0,0,0))

        #ゲームに登場する人・物・背景の位置アップデート
        bg_taiki.update()

        #画面上に登場する人・物・背景を描画
        
        bg_taiki.draw(screen)
        #画面の実表示
        pygame.display.update()

        #イベント処理
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                po=1
                break
        if po==1:
            break

        #描画スピードの調整
        clock.tick(30)
    #一問目出題
    po=0
    start=time.time()
    right=0
    left=0
    while True:
        #画面をクリア
        screen.fill((0,0,0))
        
        #ゲームに登場する人・物・背景の位置アップデート
        bg_img_q_1.update(screen)
        bg_img_q_1.draw(screen)
        a_1_True.update(screen)
        a_1_false.update(screen)
        now=time.time()
        if 4<=(10-(now-start)) and (10-(now-start))<=5:
            #上の(任意の正整数-(now-start))の任意の正整数はシンキングタイム(おそらく一分を越すとうごかない)
            five.draw(screen)
        elif 3<(10-(now-start))<4:
            four.draw(screen)
        elif 2<(10-(now-start))<3:
            three.draw(screen)
        elif 1<(10-(now-start))<2:
            two.draw(screen)
        elif 0<(10-(now-start))<1:
            one.draw(screen)
        elif (10-(now-start))<0:
            one.undraw()
            break
        #画面上に登場する人・物・背景を描画
        

        
        
        #画面の実表示
        pygame.display.update()

        #イベント処理
        for event in pygame.event.get():
            if event.type==QUIT:
                os._exit()
            if event.type==K_LEFT:
                right=1
                left=0
            if event.type==K_RIGHT:
                left=1
                right=0    
        #後でカウントダウンを画像にする
        
        #描画スピードの調整
        clock.tick(30)
    #正誤判定してぶんきする
    #ansに出題写真の時にstrで正解がleftかrightか書いておく
    if left==1:
        if ans=="left":
            while True:
                #画面をクリア
                screen.fill((0,0,0))

                #ゲームに登場する人・物・背景の位置アップデート
                bg_img_a_1_True.update(screen)

                #画面上に登場する人・物・背景を描画
                bg_img_a_1_True.draw(screen)
        
                #画面の実表示
                pygame.display.update()

                #イベント処理
                #後で時間がたって回答したらbreakするようにする
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        po=1
                        break
                if po==1:
                    break
                #描画スピードの調整
                clock.tick(30)
        
    po=0
    while True:
        #画面をクリア
        screen.fill((0,0,0))

        #ゲームに登場する人・物・背景の位置アップデート
        bg_img_a_1_True.update(screen)

        #画面上に登場する人・物・背景を描画
        bg_img_a_1_True.draw(screen)
        
        #画面の実表示
        pygame.display.update()

        #イベント処理
        #後で時間がたって回答したらbreakするようにする
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                po=1
                break
        if po==1:
            break
        #描画スピードの調整
        clock.tick(30)

if __name__ == "__main__":
    main()
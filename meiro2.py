#a
import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    bx=250
    by=150
    hx=250
    hy=150
    hx2=hx#1フレーム前の座標
    hy2=hy
    cx=350
    cy=150
    kx=0
    ky=0
    stk=[]
    start=[0,0]
    goal=[5,5]
    kakunin=[]
    map=[[0,0,0,0,1,1],
        [0,1,0,1,1,0],
        [0,1,0,0,0,0],
        [0,0,1,0,1,0],
        [1,1,0,1,1,0],
        [0,0,0,0,0,0],
        ]
    gPng = pygame.image.load("ball.png").convert_alpha()   #画像を読み込む   
    gPng = pygame.transform.scale(gPng, (50,50)) #200x200に画像を拡大
    gPng2 = pygame.image.load("cube.png").convert_alpha()   #画像を読み込む   
    gPng2 = pygame.transform.scale(gPng2, (50,50)) #200x200に画像を拡大

    def meiro(map,start,goal):
        stk.append(start)  #スタート地点をスタックする
        top=stk.pop()
        hx=top[0]
        hy=top[1]
        kakunin.append(top)
        
        # if top==goal:
        #     break
        hy=hy-1#上確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hy<0:#場外だったら外す
            stk.pop()
        elif k2== False:#一度通っていたら外す
            stk.pop()

        #調べる位置に戻る
        hy=top[1]

        hy=hy+1#下確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hy<150+60*50:#場外だったら外す
            stk.pop()        
        elif k2== False:#一度通っていたら外す
            stk.pop()
        
            
            
        hx=hx-1#左確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hx<0:#場外だったら外す
            stk.pop()
        elif k2== False:#一度通っていたら外す
            stk.pop()
        
        hx=top[0]#調べる位置に戻る
        
        
        hx=hx+1#右確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hx>250+6*50:#場外だったら外す
            stk.pop()
        elif k2== False:#一度通っていたら外す
            stk.pop()
        
            

        return kakunin
            
            
            
            
            
            

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        
        pygame.draw.rect(screen, (255,255,255), Rect(bx,by,50,50))    # ■
        for g in range(6):
            for r in range(6):
                if map[g][r]==0:
                    pygame.draw.rect(screen, (240,240,240), Rect(bx+r*50,by+g*50,50,50),2)    # ■
                elif map[g][r]==1:
                    pygame.draw.rect(screen, (100,100,100), Rect(bx+r*50,by+g*50,50,50))    # ■
        screen.blit(gPng ,Rect(hx,hy,1,1))#オブジェクトを指定の座標に表示
        screen.blit(gPng2 ,Rect(cx,cy,1,1))#オブジェクトを指定の座標に表示
        pygame.draw.rect(screen, (50,50,50), Rect(bx,by,300,300),1)    # ■
        
        pygame.display.update()                                       # 画面更新
        
        kakunin=meiro(map,start,goal)
        
        
        #----------------------------------------------------
        stk.append(start)  #スタート地点をスタックする
        top=stk.pop()
        if top==goal:
            break
        #----------------------------------------------------
        
        
            
          
        #スタート地点をスタックする
        #以下繰り返し
        #    スタックからデータをとってくる
        #    とってきたデータがゴールか判定する
        #    ゴールなら繰り返しを抜ける
        #    x-1,x+1,y-1,y+1をして進めた方向をスタックする
        #    一回通った場所と壁と場外以外は進むことができる
        
        


        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら
                pygame.quit()             
                sys.exit()                # 終了
if __name__ == "__main__":
    main()


import pygame
from pygame.locals import *
import sys
def meiro(map,start,goal,g,r,hx,hy,stk,kakunin):
    stk.append(start)  #スタート地点をスタックする
    while True:
        print("stk=",stk)
        top=stk.pop()
        if top==goal:
            break
        hx=top[0]
        hy=top[1]
        kakunin.append(top)        
        print("top=",top)
        print("kakunin=",kakunin)

        hy=hy-1#上確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hy<0:#場外だったら外す
            stk.pop()
        elif k2== True:#一度通っていたら外す
            stk.pop()

        #調べる位置に戻る
        hy=top[1]

        hy=hy+1#下確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hy>g:#場外だったら外す
            stk.pop()        
        elif k2== True:#一度通っていたら外す
            stk.pop()
            
            
            
        hx=hx-1#左確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hx<0:#場外だったら外す
            stk.pop()
        elif k2== True:#一度通っていたら外す
            stk.pop()
        
        hx=top[0]#調べる位置に戻る
        
        
        hx=hx+1#右確認
        stk.append([hx,hy])#とりあえず積む
        k2=[hx,hy] in kakunin
        if map[hy][hx]==1:#壁だったら外す
            stk.pop()
        elif hx>r:#場外だったら外す
            stk.pop()
        elif k2== True:#一度通っていたら外す
            stk.pop()
        
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    hx=0
    hy=0
    stk=[]
    start=[0,0]
    goal=[5,5]
    kakunin=[]#通った場所を入れておく配列 結果的に二次元配列になる
    map=[[0,0,0,0,1,1],
        [0,1,0,1,1,0],
        [0,1,0,0,0,0],
        [0,0,1,0,1,0],
        [1,1,0,1,1,0],
        [0,0,0,0,0,0],
        ]
    g=len(map)
    r=len(map[0])
    meiro(map,start,goal,g,r,hx,hy,stk,kakunin)  
main()

            
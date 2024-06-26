
import pygame
from pygame.locals import *
import sys
def meiro(map,start,goal,stk,kakunin,path):
    g=len(map)
    r=len(map[0])
    stk.append([start,path])  #スタート地点をスタックする  
    while True:
        print("----------")
        print("@8 stk=",stk)
        top2=stk.pop()#通った場所の座標#stkが今まで通った場所も含んでいるからtop2を使っている
        #stkにはトレース図の赤い数字と青い数字が積まれている、ここから一番上をとってきたのがtop2である。
        #赤い数字だけ取り出したいので15行目を行った。
        top=top2[0]#赤い数字
        blue=top2[1]#青い数字
        
        print(f"@15 {top=}")
        print(f"@16{top[1]=}")
        print(f"@11 {stk=}")
        if top==goal:
            print("ゴール")
            break
        hr=top[1]#右の座標
        hg=top[0]#左の座標
        kakunin.append(top) 
        path.append(top)        
        print(f"@26,{top=}")
        #print("@22kakunin=",kakunin)
        
        
        nr=top[1]#右の座標
        ng=top[0]#左の座標
        print(f"@28{ng=}{hg=}")
        ng=hg-1#上確認
        if ng>=0 :
            print(f"@26 {ng=} {nr=}")
            stk.append([ng,nr])#とりあえず積む
            print(f"@28 {stk=} {ng=} {nr=}")
            k2=[ng,nr] in kakunin
            if map[ng][nr]==1:#壁だったら外す
                stk.pop()
            elif k2== True:#一度通っていたら外す
                stk.pop()
        print(f"@32上 {stk=}")
        #調べる位置に戻る
        

        ng=hg+1#下確認
        if ng<g:
            stk.append([ng,nr])#とりあえず積む
            print(f"@35 {stk=}")
            k2=[ng,nr] in kakunin
            if map[ng][nr]==1:#壁だったら外す
                stk.pop() 
            elif k2== True:#一度通っていたら外す
                stk.pop()
        print(f"@45下 {stk=}")
            
        ng=top[0]    
            
        nr=hr-1#左確認
        if nr>=0:
            stk.append([ng,nr])#とりあえず積む
            k2=[ng,nr] in kakunin
            if map[ng][nr]==1:#壁だったら外す
                stk.pop()
            elif k2== True:#一度通っていたら外す
                stk.pop()
        print(f"@57左 {stk=}")

        
        
        nr=hr+1#右確認
        blue.append(top)
        if nr<r:
            stk.append([ng,nr])#とりあえず積む
            print(f"@64{stk=}")
            k2=[ng,nr] in kakunin
            print(f"@66{ng=} {nr=}")
            if map[ng][nr]==1:#壁だったら外す
                stk.pop()
                print("68")
            elif k2== True:#一度通っていたら外す
                stk.pop()
                print("71")
        print(f"@67右 {stk=}")
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    nr=0
    ng=0
    stk=[]
    start=[0,0]
    goal=[3,3]
    kakunin=[]#通った場所を入れておく配列 結果的に二次元配列になる
    path=[]
    #00,01,02,12,22が正しい
    map=[[0,0,0,0],
        [0,1,0,1],
        [0,1,0,0],
        [0,0,1,0],
        ]
    
    meiro(map,start,goal,stk,kakunin,path)  
main()

            
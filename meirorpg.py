import pygame
from pygame.locals import *
import sys
class Player():
    def __init__(self):
        self.pg=0
        self.pr=0
        self.gct=0
        self.bt=False
        self.kf=False
    def update(self,map):
        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら
                pygame.quit()             
                sys.exit()                # 終了
            elif event.type == KEYDOWN: 
                self.kf=True
                if event.key==K_LEFT:
                    self.pr=self.pr-1
                    if map[self.pg][self.pr]==1:
                        self.pr=self.pr+1
                elif event.key==K_RIGHT:
                    if self.pr<len(map[0])-1:
                        if map[self.pg][self.pr+1]==0:
                            self.pr=self.pr+1
                elif event.key==K_UP:
                    self.pg=self.pg-1
                    if map[self.pg][self.pr]==1:
                        self.pg=self.pg+1

                elif event.key==K_DOWN:
                    if self.pg<len(map)-1:
                        if map[self.pg+1][self.pr]==0:
                            self.pg=self.pg+1

            if self.pg<0:
               self.pg=self.pg+1
            elif self.pr<0:
                self.pr=self.pr+1
            
            if [self.pg,self.pr]==[0,0]:
                self.bt=True
            if [self.pg,self.pr]==[7,7] and self.kf==True and self.bt==True:
                self.gct=self.gct+1
                self.kf=False
                self.bt=False
                print(f"{self.gct=}")
        if self.gct==3:
            print("クリア")
        return (self.pg,self.pr)
    def draw(self,screen):
        pygame.draw.circle(screen,(10,10,255),(self.pr*50+25,self.pg*50+25),25)  #プレイヤー     
class Teki():
    def __init__(self,g,r):
        self.eg=g
        self.er=r
        self.ct=0
        self.status=False#敵がプレイヤーを捕まえた
    def update(self,P1,map):
        start=(self.eg,self.er)
        goal=(P1.pg,P1.pr)
        
        
        ans=meiro(map,start,goal)
        if len(ans)!=1:
            print(f"{ans=}")
            self.ct=self.ct+1
            if self.ct%10==0:
                self.eg=ans[1][0]
                self.er=ans[1][1]
        if start==goal:
            print( "ゲームオーバー")
            self.status=True
    def draw(self,screen):
        pygame.draw.circle(screen,(255,100,10),(self.er*50+25,self.eg*50+25),25)  # 敵
def meiro(map,start,goal):
    stk=[]#スタック [[中身],[中身]...]  となっていて中身は[[着目点],[パス]]という構成
    path=[]#正解のパス(トレース図の青い数字)
    visited=[]#一度通った場所を入れておく配列（場所は座標なので全体は２次元配列）
    stk.append([start,path])  #スタート地点をスタックする
    while True:
        top=stk.pop(0)   #スタックトップを取り出し着目点とパスに分解
        point=top[0]    #着目点（トレース図の黄色い数字）
        path=top[1]     #パス（トレース図の青い数字）
        if point == goal:#着目点がゴールなら修了
            return path
        visited.append(point)  #着目点をvisitedに追加していく
        dydx=[(-1,0),(1,0),(0,-1),(0,1)]#(dy,dx)は上下左右の差分データ#(1,1)の上は(0,1)下は(2,1)左は(1,0)右は(1,2)
        for i in range(4):
            ny=point[0]+dydx[i][0]  #新しい座標の計算
            nx=point[1]+dydx[i][1]
            if 0<=ny<len(map) and 0<=nx<len(map[0]):#範囲内なら
                tmp = path.copy()   #一時的な変数にパスをコピー
                tmp.append(point)   #tmpに着目点を追加
                stk.append([(ny,nx),tmp])#とりあえずスタックに積んでしまう（新しい着目点と新しいパス）
                if map[ny][nx]==1:#壁だったらスタックから外す
                    stk.pop()
                elif (ny,nx) in visited:#一度通っていたらスタックから外す
                    stk.pop()        
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    px=120
    py=100
    
    
    map=[[0,0,0,0,0,0,1,1],
        [0,1,0,0,1,0,1,0],
        [0,1,0,1,1,0,0,0],
        [0,1,0,0,1,0,0,0],
        [0,0,1,1,1,1,1,0],
        [0,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,0],
        [0,0,1,0,0,1,1,0]]
    P1=Player()
    T1=Teki(5,4)
    T2=Teki(6,6)
    ck = pygame.time.Clock()
    ct=0

    
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        pygame.draw.line(screen, (0,255,0), (0,200), (100,300), 2)    # 線
        for g in range(len(map)):
            y=g*50
            for r in range(len(map[0])):
                x=r*50
                if map[g][r]==1:
                    pygame.draw.rect(screen, (255,0,0), Rect(x,y,50,50))  
                else:
                    pygame.draw.rect(screen, (60,0,0), Rect(x,y,50,50))    # ■
        pgr=P1.update(map)
        P1.draw(screen)
  
        T1.update(P1,map)
        T1.draw(screen)
        T2.update(P1,map)
        T2.draw(screen)
        if T1.status==True or T2.status==True:
            break
        ck.tick(30) #1秒間で30フレームになるように33msecのwait

        pygame.display.update()                                       # 画面更新

        
             
                
if __name__ == "__main__":
    main()

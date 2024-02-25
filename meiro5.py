def meiro(map,start,goal):
    stk=[]#スタック [[中身],[中身]...]  となっていて中身は[[着目点],[パス]]という構成
    path=[]#正解のパス(トレース図の青い数字)
    visited=[]#一度通った場所を入れておく配列（場所は座標なので全体は２次元配列）
    stk.append([start,path])  #スタート地点をスタックする
    while True:
        top=stk.pop(0)   #スタックボトムを取り出し着目点とパスに分解
        point=top[0]    #着目点（トレース図の黄色い数字）
        path=top[1]     #パス（トレース図の青い数字）
        if point == goal:#着目点がゴールなら修了
            print("goal!!")
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
    start=(0,0)#
    goal=(3,0)
    map=[[0,0,0,0],
        [0,1,0,1],
        [0,1,0,0],
        [0,0,0,0],
        ]
    ans=meiro(map,start,goal)
    print(ans)
main()
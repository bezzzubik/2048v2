import movefunc as move

def eas(memor):
    k=memor+3*(1-memor%2)
    return k

def eas2(memor, logmass, oldlogmass):

    if memor==1 and not logmass:
        return 3
    elif memor==3:
        return 6
    elif memor==6:
        return 2
    
    if oldlogmass:
        return 5   

    if logmass or memor == 4:
        return 7
    else:
        return 1


def kf():
    koef=[[0.8, 0.85, 0.9, 1],
          [0.6, 0.6, 0.6, 0.6],
          [0.3, 0.3, 0.3, 0.3],
          [0.1, 0.1, 0.1, 0.1]]
    return koef


def botmid(oldm):
    k=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.,0.,0.,0.],[0.,0.,0.,0.]]
    m=[ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    newm=[[],[],[],[]]
    koef=[[0.0,0.0,0.0,0.0],
          [0.0,0.0,0.0,0.0],
          [0.0,0.0,0.0,0.0],
          [0.0,0.0,0.0,0.0]]
    for p in range(4):
        koef=kf()

        if oldm[0][3]<oldm[0][2]:
            for i in range(4):
                koef[i].reverse()
            koef=list(map(list, zip(*koef)))
            for i in range(4):
                koef[i].reverse()
        
        m=move.mat([oldm[0].copy(),oldm[1].copy(),oldm[2].copy(),oldm[3].copy()], p*2+1)
        for l in range(4):
            m=move.mat(m, p*2+1)
            if m != oldm:
                for i in range(4):
                    for j in range(3,-1, -1):
                        k[p][l]+=m[i][j]*koef[i][j]
                        if (i!=3 and m[i][j]==m[i+1][j]) or (j!=0 and m[i][j]==m[i][j-1]):
                            k[p][l]+=m[i][j]*koef[i][j]/2
                        if (p==1 or p==5) and m[0].count(0)!=0 and oldm[0][3]>=oldm[0][2]:
                            k[p][l]/=2
                        if (p==5 or p==1) and oldm[0][3]<oldm[0][2]:
                            k[p][l]/=2
    for i in range(4):
        k[i]=max(k[i])
    return (k.index(max(k)))*2+1
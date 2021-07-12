def mat(m, k):
    if k > 4:
        if k==5:
            m.reverse()

        m=list(map(list, zip(*m)))

        for i in range(4):
           m[i]=newmat(m[i])

        m=list(map(list, zip(*m)))
    else:
        if k == 1:
           m[0].reverse()
           m[1].reverse()
           m[2].reverse()
           m[3].reverse()
           

        for i in range(4):
            m[i]=newmat(m[i])
           
    if k==5:
            m.reverse()
    elif k == 1:
           m[0].reverse()
           m[1].reverse()
           m[2].reverse()
           m[3].reverse()

    return m


def newmat(m):
    global score
    k=m.count(0)
    while k!=0:
        m.remove(0)
        m.append(0)
        k-=1

    for i in range(3):
        if m[i]==m[i+1] and m[i]!=0:
            m[i]*=2
            m.pop(i+1)
            m.append(0)

    return m


def scorecon(oldm, m):
    for i in range(4):
        oldm.extend(oldm[0])
        oldm.pop(0)
        m.extend(m[0])
        m.pop(0)
    oldm.sort()
    m.sort()
    sc=0
    for i in range(16):
        if oldm.count(oldm[i]) > m.count(oldm[i]) and oldm[i]!=0:
                coold=oldzn=oldm[i]
                oldm[i]=0
                for i in range(16):
                    if oldm[i]==oldzn:
                        oldm[i]*=2
                        oldzn*=2
                        sc+=oldzn
                        break
    return sc

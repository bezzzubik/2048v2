import pygame
import random as r
import movefunc as move
import bot
import datetime as d

def drawBack(win):
    win.fill((224, 255, 255))
    pygame.draw.rect(win, (169, 169, 169), (10, 35, 407, 405))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(win, (220, 220, 220), (15+100*j+3, 40+100*i+3, 90, 90))
    pass


def gener(m):
    for i in range(4):
        for j in range(4):
            m[i][j]=0
    return ran(m)






def endgame(m):
    k=m[0].count(0)+m[1].count(0)+m[2].count(0)+m[3].count(0)
    if k==0:
        for i in range(3):
            for j in range(3):
                if m[i][j]==m[i+1][j] or m[i][j]==m[i][j+1]:
                    return False
        for j in range(3):
            if m[3][j]==m[3][j+1]:
                return False
        return True
    else:
        return False




def ran(m):
    k=r.randint(0, 15)
    i=int(k%4)
    j=int(k/4)
    while m[i][j] != 0:
            k+=1
            if k==16:
                k=0
            i=int(k%4)
            j=int(k/4)
    c=r.randint(7, 16)
    m[i][j]=int(2+2*(c&16)/16)
    return m



def prgame(s, w):
    for i in range(4):
        for j in range(4):
            if s[i][j] != 0:
                pygame.draw.rect(w, (255, 250, 250), (15+100*j+3, 40+100*i+3, 90, 90))
                txt=font.render(str(s[i][j]), True, (0, 0, 0))
                w.blit(txt, (43+100*j-10*(len(str(s[i][j]))-1)+3, 40+100*i+20+3))
    pass


pygame.init()
win = pygame.display.set_mode((430,490))

pygame.display.set_caption("2048")

run = True

mass=[ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
old_mass=[ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
older_mass=[ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]


mass=gener(mass)
font=pygame.font.SysFont("arial", 50)
re=pygame.font.SysFont("timesnewroman", 32)
co=pygame.font.SysFont("timesnewroman", 24)
botnf=False
endg=False
memor=4
with open('global score.txt', 'r') as f:
    record=int(f.read().split('\n')[0])
logm=True
score=0
count_game=1
with open('game.txt', 'a') as f:
    f.write("Koef:"+str(bot.kf())+'\n')
while run:

    pygame.time.delay(100)
    if record<score:
        with open('global score.txt', 'w') as f:
            f.write(str(score)+'\n')
            f.write("Koef:"+str(bot.kf())+'\n')
        record=score
    if endg:
       txt=font.render("Game over", True, (220, 20, 60))
       win.blit(txt, (105, 50+90+5+75))
       txt=re.render("press \"r\" to restar", True, (220, 20, 60))
       win.blit(txt, (98, 100+75))
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    endg=False
                    mass=gener(mass)
                    count_game+=1
                    score=0
       if botnf:
            with open('game.txt', 'a') as f:
                s=d.datetime.now()
                f.write("game:"+str(count_game)+'\n')
                f.write("Score:"+str(score)+'\n')
                f.write("Time:"+str(str(s.hour)+':'+str(s.minute)+':'+str(s.second))+'\n')
                f.write("Max:"+str(max([max(mass[0]), max(mass[1]),max(mass[2]), max(mass[3])] ))+'\n\n')
                
            mass=gener(mass)
            score=0
            endg=False
            count_game+=1
       
    else:
        old_mass=[mass[0].copy(), mass[1].copy(), mass[2].copy(), mass[3].copy()]
        k=0
        if botnf:
            pygame.time.delay(300)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_b:
                      botnf=not botnf
#            бот1 - по кругу
#            k=bot.eas(memor)
#            memor=memor%4+1

#            бот2 - вверх\вправо
#            memor=bot.eas2(memor, logm, older_mass==mass)
#           if memor == 6:
#              older_mass=[mass[0].copy(), mass[1].copy(), mass[2].copy(), mass[3].copy()]
#                k=7
#            elif memor == 2:
#                k=1
#                memor=4
#            else:
#                k=memor
#            бот3 - ветка алгоритмов
            k=bot.botmid(old_mass)
        else:

           for event in pygame.event.get():
             if event.type == pygame.QUIT:
                    run=False
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    k=3
                elif event.key == pygame.K_RIGHT:
                    k=1
                elif event.key ==pygame.K_UP:
                    k=7
                elif event.key == pygame.K_DOWN:
                    k=5
                elif event.key == pygame.K_b:
                    botnf=not botnf
                elif event.key == pygame.K_r:
                    mass=gener(mass)
                    score=0
        if k!=0:
           mass=move.mat(mass, k)
           logm=old_mass!=mass
           if logm:
               score+=move.scorecon([old_mass[0].copy(),old_mass[1].copy(),old_mass[2].copy(),old_mass[3].copy()], [mass[0].copy(),mass[1].copy(),mass[2].copy(),mass[3].copy()])
               mass=ran(mass)
           endg=endgame(mass)
        drawBack(win)
        prgame(mass, win)
    t=re.render("Press \"b\" to on or off bot", True, (35, 35, 35))
    win.blit(t, (10, 450))
    t=re.render("Record:"+str(record), True, (35, 35, 35))
    win.blit(t, (10, 0))
    t=re.render("Score:"+str(score), True, (35, 35, 35))
    win.blit(t, (250, 0))
    t=co.render("Game:"+str(count_game), True, (35, 35, 35))
    win.blit(t, (340, 454))

    pygame.display.update()

pygame.quit()


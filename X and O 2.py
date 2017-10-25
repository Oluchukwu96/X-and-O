#Game of X and O hope it works
from graphics import *
from random import randrange
win=GraphWin("X and O",300,300)
win.setCoords(0.0,0.0,3.0,3.0)
p1=Point(0.5,0.5)
p2=Point(0.5,1.5)
p3=Point(0.5,2.5)
p4=Point(1.5,0.5)
p5=Point(1.5,1.5)
p6=Point(1.5,2.5)
p7=Point(2.5,0.5)
p8=Point(2.5,1.5)
p9=Point(2.5,2.5)
p10=Point(4,4)
def main():
    Line(Point(0,1),Point(3,1)).draw(win)
    Line(Point(0,2),Point(3,2)).draw(win)
    Line(Point(1,0),Point(1,3)).draw(win)
    Line(Point(2,0),Point(2,3)).draw(win)

def X(point):
    x=point.getX()
    y=point.getY()
    Line1=Line(Point((x-0.5),(y-0.5)),Point((x+0.5),(y+0.5)))
    Line2=Line(Point((x-0.5),(y+0.5)),Point((x+0.5),(y-0.5)))
    Line1.setFill('red')
    Line2.setFill('red')
    Line1.draw(win)
    Line2.draw(win)
def O(point):
    circle=Circle(point,0.5)
    circle.setFill('blue')
    circle.draw(win)
def play():
    pos=win.getMouse()
    x=pos.getX()
    y=pos.getY()
    if x<1 and y<1:
        grid=p1
    if x<1 and y<2 and y>1:
        grid=p2
    if x<1 and y<3 and y>2:
        grid=p3
    if x<2 and x>1 and y<1:
        grid=p4
    if x<2 and x>1 and y<2 and y>1:
        grid=p5
    if x<2 and x>1 and y<3 and y>2:
        grid=p6
    if x<3 and x>2 and y<1:
        grid=p7
    if x<3 and x>2 and y<2 and y>1 :
        grid=p8
    if x<3 and x>2 and y<3 and y>2 :
        grid=p9
    return grid
def convert(grid):
    if grid==p1:
        grid=1
    if grid==p2:
        grid=2
    if grid==p3:
        grid=3
    if grid==p4:
        grid=4
    if grid==p5:
        grid=5
    if grid==p6:
        grid=6
    if grid==p7:
        grid=7
    if grid==p8:
        grid=8
    if grid==p9:
        grid=9 
    return grid
def convertc(grid):
    if grid==1:
        grid=p1
    if grid==2:
        grid=p2
    if grid==3:
        grid=p3
    if grid==4:
        grid=p4
    if grid==5:
        grid=p5
    if grid==6:
        grid=p6
    if grid==7:
        grid=p7
    if grid==8:
        grid=p8
    if grid==9:
        grid=p9   
    return grid  
def playgame():
    N1=[]
    N2=[]
    N3=[]
    D1=[p1,p2,p3,p4,p5,p6,p7,p8,p9]
    x=0
    no=0
    PL=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    while x==0:
        no+=1
        grid=play()
        while grid in N1:
            grid=play()
        if len(N1)%2==0:
            turn=X
        else:
            turn=O
        if turn==X:
            n=convert(grid)
            N2.append(n)
            N2.sort()
        if turn==O:
            n=convert(grid)
            N3.append(n)
            N3.sort()
        for a in PL:
            if all(i in N2 for i in a):
                print("X is the winner")
                x=1
            if all(i in N3 for i in a):
                print("O is the winner")
                x=1
        if len(N1)==9:
            print("You drew")
            x=1
        N1.append(grid)
        D1.remove(grid)
        turn(grid)
def thinkp(D1,PL,N2,N3):
        for i in D1:
            n=convert(i)
            score=0
            L=[]
            for a in PL:
                L=[]
                for j in a:
                    if j in L1:
                       L.append(j)        
                if len(L)==2 and L[0] in N3 and L[1] in N3 and n in a:
                    score+=4
                if len(L)==2 and L[0] in N2 and L[1] in N2 and n in a:
                    score+=8
        return score       
        
def complay(D1,PL,N1,N2,N3,whot):
    lscore=0
    one=randrange(1,25)
    L1=[]
    for i in N1:
        L1.append(convert(i))
    if whot<5:
        if one>9:
            chosen=p5
        else:
            chosen=convertc(one)
    else:
        one=randrange(1,30)
        if one>9 and one<16:
            chosen=p3
        if one>15 and one<21:
            chosen=p1
        if one>20 and one<26:
            chosen=p7
        if one>25 and one<31:
            chosen=p9
        if one<10:
            chosen=convertc(one)
    while chosen not in D1:
        one=randrange(1,9)
        chosen=convertc(one)
    for i in D1:
        n=convert(i)
        score=0
        L=[]
        Pl=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for a in PL:
            L=[]
            no=0
            for j in a:
                if j in L1:
                    L.append(j)        
            if len(L)==2 and L[0] in N2 and L[1] in N2 and n in a:
                score+=4
            if len(L)==2 and L[0] in N3 and L[1] in N3 and n in a:
                score+=8
            if whot>4 and len(L)==2 and L[0] in N3 and L[1] in N3 and n in a:
                score+=5
            if whot>4 and len(L)==2 and L[0] in N2 and L[1] in N2 and n in a:
                score+=15    
            if len(L)==2 and L[0] in N2 and L[1] in N3 and whot<5 :
                score-=0.1
            if len(L)==2 and L[0] in N3 and L[1] in N2 and whot<5:
                score-=0.1
            if len(N1)!=3 and len(L)==1 and L[0] in N3 and n in a and whot<5:
                score+=0.2
            if whot>4 and len(L)==1 and L[0] in N2 and n in a:
                score+=3
                Pl.remove(a)
                for b in Pl:
                    if len(L)==1 and L[0] in N2 and n in b:
                        score+=0.1
            if whot>4 and len(L)==1 and L[0] in N3 and n in a:
                score+=1
            if whot>4 and len(L)==2 and any(i in N2 for i in L) and any(i in N2 for i in L) and n in a:
                score+=2
        if score>lscore:
            lscore=score
            chosen=i
        
    return chosen
def playcom():
    N1=[]
    N2=[]
    N3=[]
    D1=[p1,p2,p3,p4,p5,p6,p7,p8,p9]
    x=0
    PL=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    whot=randrange(1,30)
    while x==0:
        if len(N1)%2==0:
            turn=X
        else:
            turn=O
        if whot<5:
            if turn==X:
                grid=play()
                while grid in N1:
                    grid=play()
            else:
                grid=complay(D1,PL,N1,N2,N3,whot)    
        else:
            if turn==X:
                grid=complay(D1,PL,N1,N2,N3,whot)
            else:
                grid=play()
                while grid in N1:
                    grid=play()
        if turn==X:
            n=convert(grid)
            N2.append(n)
            N2.sort()
        if turn==O:
            n=convert(grid)
            N3.append(n)
            N3.sort()
        for a in PL:
            if all(i in N2 for i in a):
                print("X is the winner")
                x=1
            if all(i in N3 for i in a):
                print("O is the winner")
                x=1
        N1.append(grid)
        D1.remove(grid)
        turn(grid)
                
    
    
        
        
main()
playcom()

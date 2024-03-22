import random
r1=[['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','','']]
r2=[['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','','']]
class Score:
    s=0
def adder(l, rc, d):
    if rc == 'r':
        for i in range(4):
            if d == -1:
                j = 0
                while j < 3:
                    if l[i][j] != '':
                        k = j + 1
                        while k < 4:
                            if l[i][k] != '':
                                if l[i][j] == l[i][k]:
                                    if l==r1:
                                        Score.s+=l[i][j]
                                    l[i][j] *= 2
                                    l[i][k] = ''
                                
                                break
                            k += 1
                    j += 1
            else:
                j = 3
                while j > 0:
                    if l[i][j] != '':
                        k = j - 1
                        while k >= 0:
                            if l[i][k] != '':
                                if l[i][j] == l[i][k]:
                                    if l==r1:
                                        Score.s+=l[i][j]
                                    l[i][j] *= 2
                                    l[i][k] = ''
                                
                                break
                            k -= 1
                    j -= 1
    elif rc == 'c':
        for i in range(4):
            if d == -1:
                j = 0
                while j < 3:
                    if l[j][i] != '':
                        k = j + 1
                        while k < 4:
                            if l[k][i] != '':
                                if l[j][i] == l[k][i]:
                                    if l==r1:
                                        Score.s+=l[j][i]
                                    l[j][i] *= 2
                                    l[k][i] = ''
                                
                                break
                            k += 1
                    j += 1
            else:
                j = 3
                while j > 0:
                    if l[j][i] != '':
                        k = j - 1
                        while k >= 0:
                            if l[k][i] != '':
                                if l[j][i] == l[k][i]:
                                    if l==r1:
                                        Score.s+=l[j][i]
                                    l[j][i] *= 2
                                    l[k][i] = ''
                                
                                break
                            k -= 1
                    j -= 1
def display(l):
    for i in range(4):
        for j in range(4):
            if l[i][j]=='':
                print('_',end='\t')
            else:
                print(l[i][j],end='\t')
        print('\n')
def mover(l,rc,d):
    if rc=='r':
        for i in range(4):
            x=4 if d==-1 else -5
            index=0 if d==-1 else -1
            j=0 if d==-1 else -1
            while(j!=x):
                if l[i][j]!='':
                    l[i][index]=l[i][j]
                    l[i][j]='' if index!=j else l[i][j]
                    if d==-1:
                        index+=1
                    else:
                        index-=1
                if d==-1:
                    j+=1
                else:
                    j-=1
    elif rc=='c':
        for i in range(4):
            index=0 if d==-1 else -1
            x=4 if d==-1 else -5
            j=0 if d==-1 else -1
            while(j!=x):
                if l[j][i]!='':
                    l[index][i]=l[j][i]
                    l[j][i]='' if index!=j else l[j][i]
                    if d==-1:
                        index+=1
                    else:
                        index-=1
                if d==-1:
                    j+=1
                else:
                    j-=1
                
def isover():
    for i in range(4):
        for j in range(4):
            r2[i][j]=r1[i][j]
    adder(r2,'r',-1)
    mover(r2,'r',-1)
    adder(r2,'c',-1)
    mover(r2,'c',-1)
    adder(r2,'r',1)
    mover(r2,'r',1)
    adder(r2,'c',1)
    mover(r2,'c',1)
    for i in range(4):
        for j in range(4):
            if(r1[i][j]!=r2[i][j]):
                return 0 
    return 1
    
def iswon():
    for i in r1:
        for j in i:
            if j==2048:
                return 1
    return 0

def rangen(d):
    if(d==0):
        a=random.randint(0,3)
        b=random.randint(0,3)
        r1[a][b]=2
        while (c:=random.randint(0,3))==a:
            c=random.randint(0,3)
        r1[c][a]=2
    else:
        empty_cells = [(i, j) for i in range(4) for j in range(4) if r1[i][j] == '']
        if empty_cells:
            cell = random.choice(empty_cells)
            r1[cell[0]][cell[1]] = 2
if __name__=='__main__':
    print("w->up\na->left\ns->down\nd->right\n")
    rangen(0)
    while(1):
        display(r1)
        x=input("Enter choice:")
        if x=='x' or iswon() or isover():
            break
        if x=='a':
            adder(r1,'r',-1)
            mover(r1,'r',-1)
            rangen(1)
        elif x=='w':
            adder(r1,'c',-1)
            mover(r1,'c',-1)
            rangen(1)
        elif x=='d':
            adder(r1,'r',1)
            mover(r1,'r',1)
            rangen(1)
        elif x=='s':
            adder(r1,'c',1)
            mover(r1,'c',1)
            rangen(1)
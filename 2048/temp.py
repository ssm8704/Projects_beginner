def adder(l,rc,d):
    if rc=='r':
        for i in range(0,4):
            j=0
            j1=-1
            while(j!=4):
                if(j==2):
                    break
                if(l[i][j]!='' and l[i][j]==l[i][j+1]):
                    break
                j+=1
            j1=j+1
            while(j1!=4):
                if(j1==3 or l[i][j1]!=''):
                    break
                j1+=1
            if j!=4 and j!=-1 and j1!=4 and l[i][j]==l[i][j1]:
                a=l[i][j]+l[i][j1]
                if(d==-1):
                    l[i][j]=a
                    l[i][j1]=''
                else:
                    l[i][j1]=a
                    l[i][j]=''
    elif rc=='c':
        for i in range(0,4):
            j=0
            j1=-1
            while(j!=4):
                if(j==2):
                    break
                if(l[j][i]!=''):
                    break
                if(l[j][i]==l[j+1][i]):
                    break
                j+=1
            j1=j+1
            while(j1!=4):
                if(j1==3 or l[j1][i]!=''):
                    break
                j1+=1
            if j!=4 and j!=-1 and j1!=4 and l[j][i]==l[j1][i]:
                a=l[j][i]+l[j1][i]
                if(d==-1):
                    l[j][i]=a
                    l[j1][i]=''
                else:
                    l[j1][i]=a
                    l[j][i]=''
def adder1(l, rc, d):
    if rc == 'r':
        for i in range(4):
            if d == -1:
                j = 3
                while j > 0:
                    if l[i][j] != '' and l[i][j] == l[i][j - 1]:
                        l[i][j] *= 2
                        l[i][j - 1] = ''
                    j -= 1
            else:
                j = 0
                while j < 3:
                    if l[i][j] != '' and l[i][j] == l[i][j + 1]:
                        l[i][j] *= 2
                        l[i][j + 1] = ''
                    j += 1
    elif rc == 'c':
        for i in range(4):
            if d == -1:
                j = 3
                while j > 0:
                    if l[j][i] != '' and l[j][i] == l[j - 1][i]:
                        l[j][i] *= 2
                        l[j - 1][i] = ''
                    j -= 1
            else:
                j = 0
                while j < 3:
                    if l[j][i] != '' and l[j][i] == l[j + 1][i]:
                        l[j][i] *= 2
                        l[j + 1][i] = ''
                    j += 1
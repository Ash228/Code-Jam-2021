#tried to reduce memory requirement by sqeuence generation of permutations(credit:benpaulthurston/permutations) but couldnt take care of time constraint
import math
from itertools import permutations


class permute:
    n = 0
    count = 0
    def __init__(self, n):
        self.n = n
    def next(self):
        a = []
        num = self.count
        for i in range(self.n-1, 0, -1):
            f = math.factorial(i)
            c = math.floor(num / f)
            a.append(c+1)
            num = num - c*f
        self.count = self.count+1
        a.append(1)
        return self.fill(a)
    def fill(self, a):
        p = [0]*self.n
        v = self.n
        for i in range(0, len(a)):
            zeroes = 0
            for j in range(0, len(p)):
                if p[j] == 0:
                    zeroes +=1
                if zeroes == a[i]:
                    p[j] = v
                    v -= 1
                    break
        return p



def genlist(l,n1,c1):
    n2 = math.factorial(n1)
    p = permute(n1)
    for o in range(n2):
        ln = p.next()
        lnc = ln[0:]
        c = 0
        for i in range(n1-1):
            #print(ln)
            j = ln.index(min(ln[i:n1+1]))
            ln[i:j + 1] = reversed(ln[i:j + 1])
            #print(j)
            #print(i)
            c += (j)-(i)+1
            #print(c)
        #print(c)
        if c1 == c:
            return lnc
    return -1

n = int(input())
lf = []
for k in range(n):
    l = input()
    l = l.split()
    n1 = int(l[0])
    c1 = int(l[1])
    #print(n1)
    l = []
    for i in range(1,n1+1):
        l.append(i)
    #print(l)
    ln = genlist(l,n1,c1)
    if ln == -1:
        lf.append('IMPOSSIBLE')
    else:
        s = [str(i) for i in ln]
        st = " ".join(s)
        lf.append(st)
for i in range(n):
    print('Case #'+str(i+1)+": "+lf[i])

    
    
#Alternate
'''from itertools import permutations

def genlist(l,n1,c1):
    perm = permutations(l)
    for l1 in list(perm):
        ln = list(l1)
        lnc = list(l1)
        c = 0
        for i in range(n1-1):
            #print(ln)
            j = ln.index(min(ln[i:n1+1]))
            ln[i:j + 1] = reversed(ln[i:j + 1])
            #print(j)
            #print(i)
            c += (j)-(i)+1
            #print(c)
        #print(c)
        if c1 == c:
            return lnc
    return -1

n = int(input())
lf = []
for k in range(n):
    l = input()
    l = l.split()
    n1 = int(l[0])
    c1 = int(l[1])
    #print(n1)
    l = []
    for i in range(1,n1+1):
        l.append(i)
    #print(l)
    ln = genlist(l,n1,c1)
    if ln == -1:
        lf.append('IMPOSSIBLE')
    else:
        s = [str(i) for i in ln]
        st = " ".join(s)
        lf.append(st)
for i in range(n):
    print('Case #'+str(i+1)+": "+lf[i])
'''

from itertools import permutations

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

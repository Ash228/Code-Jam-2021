n = int(input())
for k in range(n):
    n1 = int(input())
    l = input()
    l = [int(l) for l in l.split()]
    ln = len(l)
    c = 0
    for i in range(ln-1):
        print(l)
        j = l.index(min(l[i:ln+1]))
        l[i:j + 1] = reversed(l[i:j + 1])
        print(j)
        c += (j)-(i)+1
        print(c)
    print(l)
    #print(c)
    print('Case #'+str(k+1)+': '+str(c))

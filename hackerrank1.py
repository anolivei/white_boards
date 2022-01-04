d = [1, 2, 3, 4, 5]
t = 10

ret = 0
for a in range(0, len(d) - 2):
    for b in range(a + 1, len(d) - 1):
        for c in range(b + 1,len(d)):
            tot = int(d[a]) + int(d[b]) + int(d[c])
            if (t >= tot):
                ret += 1
                print (d[a]," + ",d[b]," + ",d[c] , "=" , tot )
print("ret = ", ret)

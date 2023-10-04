def cx(l,x):
    c=0
    for i in l:
        if i == x:
            c += 1
    return c


n = int(input())
marks = list(map(int,input().split(" ")))
maxc = max(marks)
marks.sort()
c1 = cx(marks, marks[-1])
for i in range(len(marks)-1):
    if marks[i] == maxc:
        marks.remove(marks[i])
c2 = cx(marks, marks[-1])
print((c1-1) + (c2-1))

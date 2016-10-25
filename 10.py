input = open('/home/student/PycharmProjects/lab8/input5.txt' , 'r')
output = open('output.txt' , 'w')
sl = open('/home/student/en-ru.txt' , 'r')
sl = sl.read()
sl = sl.split()
B = []
C = []
i = 0
while i <= len(sl)-3:
    i += 3
    B.append(i)
j=2
while j <= len(sl):
    j += 3
    C.append(j)
D = dict(zip(B , C))
F = []
k=0
while k<=len(sl)-1:
    if sl[k] in D:
        F.append(D[sl[k]])
    k+=1
f=' '.join(F)
output.write(f)

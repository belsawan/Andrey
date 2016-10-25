import string
f= open('license')
text=f.read()
text=text.lower()
for i in range(len(text)):
    if text[i] in string.punctuation:
        text=text.replace(text[i], ' ')
A=list(map(str, text.split()))
B={A[i]: A.count(A[i]) for i in range(len(A))}
m=1
for i in range(len(A)):
    for k in range(10):
        if A.count(A[i])-k>m:
            m=A.count(A[i])
            l=A[i]
            print(l, m)



import string
f=open('/home/student/en-ru.txt')
g=open('/home/student/PycharmProjects/lab8/input.txt')
text=g.read()
text=text.lower()
for i in range(len(text)):
    if text[i] in string.punctuation:
        text=text.replace(text[i], ' ')
s=f.read()
s=list(map(str, s.split()))
a={s[i]: s[i+2] for i in range(len(s)-2)}
text=list(map(str, text.split()))
for i in text:
    if i in a:
        text[text.index(i)]=a[i]
print(*text)






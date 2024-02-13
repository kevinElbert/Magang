a = input()
b = a.split()
reverse = b[::-1]
l = []
for i in reverse:
     l.append(i)
print(" ". join(l))
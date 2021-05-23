v = list()

for x in range(0, 5):
    v.append(int(input('>> ')))

h = 1
s = len(v)
# Shell sort method
while h < s:
    h = 3*h+1
    
while h > 0:
    for i in range(h, s):
        aux = v[i]
        j = i
        while j > h-1 and aux <= v[j - h]: # <= - crescente; >= - decrescente
        
            v[j] = v [j - h]
            j = j - h
        
        v [j] = aux

    h = h//3

for x in v:
    print(x)

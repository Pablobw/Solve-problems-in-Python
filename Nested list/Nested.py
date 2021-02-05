lista = []
for _ in range(int(input())):
    nombre = input()
    nota = float(input())
    lista.append([nombre, nota])

lista.sort(key = lambda x: float(x[1]))

new_lst = []

min_mark = lista[0][1]
count = 0

for i in range(len(lista)):
    if min_mark == lista[i][1]:
        count = count+1

if count > 1:
    for j in range(count - 1):
        lista.pop(0)
for i in range(len(lista)):
    for j in range(1):
        if lista[i][1] == lista[1][1]:
            new_lst += [lista[i][0]]

sorted_lst = sorted(new_lst)
for student in sorted_lst:
    print(student)
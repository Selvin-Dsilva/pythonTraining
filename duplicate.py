temp=[12,24,35,24,88,120,155,88,120,155]

final=[]
for i in temp:
    if i not in final:
        final.append(i)
print(final)
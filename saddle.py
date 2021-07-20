A=[[2, 5, 6, 9], [-1, 4, 12, 3], [-6, 7, 3, 1], [-12, 24, 2, 11]]
rows = A
columns = list()
for x in range(len(A)) :
    suba = list()
    for y in range(len(A)) :
        suba.append(A[y][x])
    columns.append(suba)
print(suba)
print(columns)
i = 0
for x in rows :
    xxx = min(x)
    yyy = max(columns[i])
    if xxx == yyy :
        print('Sadle point exists:', xxx)
        quit()
    i += 1
print('No saddle point')

machine_part = [
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0],

]
 
m = (len(machine_part))
n = (len(machine_part[0]))
machine_name = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
part_name = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
machine = []
part = []

for i in range(0,n):
    machine.append(machine_name[i])
for j in range(0,m):
    part.append(part_name[j])
machine_part_ma = [machine, part, machine_part]

print(machine_part_ma)

weight_m = []
weight_n = []

for i in range(1, m+1):
    weight_m.append(2 ** i)
for i in range(1, n+1):
    weight_n.append(2 ** i)

def col_op(ma, a, b):
    temp = ma[0][a]
    ma[0][a] = ma[0][b]
    ma[0][b] = temp

    for i in range(m):
        temp = ma[2][i][b]
        ma[2][i][a] = ma[2][i][b]
        ma[2][i][b] = temp
    return ma

def row_op(ma, a, b):
    temp = ma[1][a]
    ma[1][a] = ma[1][b]
    ma[1][b] = temp

    r = []
    for i in range(m):
        r.append(i)

    temp = r[a]
    r[a] = r[b]
    r[b] = temp

    new_ma_cell = []

    for i in r:
        new_ma_cell.append(ma[2][i])

    new_ma = [ma[0], ma[1], new_ma_cell]

    return new_ma
def my_print(ma):
    for i in range(n):
        print('\t{}'.format(ma[0][i]),end=''),
    print(' ')
    for i in range(m):
        print(ma[1][i],end=""),
        for j in range(n):
            print('\t{}'.format(ma[2][i][j]),end=''),
        print(' ')
    return True
def col_cal(ma):
    col_sum = []
    for i in range(n):
        col_sum.append(0)

    for i in range(n):
        for j in range(m):
            col_sum[i] = col_sum[i] + ma[2][j][i] * weight_m[j]

    return col_sum

def row_cal(ma):
    row_sum = []
    for i in range(m):
        row_sum.append(0)

    for i in range(m):
        for j in range(n):
            row_sum[i] = row_sum[i] + ma[2][i][j] *weight_n[j]

    return row_sum

def gt(ma):
    re = ma
    times = 0

    while True:
        times = times +1
        axis = times %2
        changed = 0
        if axis == 0:
            csum = col_cal(re)
            for i in range(n):
                for j in range(i+1,n):
                    if csum[i] > csum[j]:
                        temp = csum[i]
                        csum[i] = csum[j]
                        csum[j] = temp
                        re = col_op(re, i , j)
                        changed = changed +1
        elif axis == 1:
            rsum = row_cal(re)
            for i in range(m):
                for j in range(i+1,m):
                    if rsum[i] > rsum[j]:
                        temp = rsum[i]
                        rsum[i] = rsum[j]
                        rsum[j] = temp
                        re = row_op(re, i, j)
                        changed =changed +1
        else:
            print("Some Error")

        if changed >=1:
            continue
        else:
            return  re
celled = gt(machine_part_ma)
my_print(celled)
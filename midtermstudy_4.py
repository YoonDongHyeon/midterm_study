
load = {
    'O': {'A': 2, 'B': 5, 'C': 4},
    'A': {'O': 2, 'B': 2, 'D': 7},
    'B': {'O': 5, 'A': 2, 'C':1, 'D': 4, 'E':3},
    'C': {'O': 4, 'B': 1, 'E': 4},
    'D': {'A': 7, 'B': 4, 'E':1, 'T':7},
    'E': {'B': 3, 'D': 1, 'T': 7, },
    'T': {'D': 5, 'E': 7}
}
starting_point = ['T']
y=[]
course =[]
sum_dist = 0
while True:
    for i in starting_point:
        for j in load[i]:
            if not j in starting_point:
                y.append([load[i][j], i, j])
    for i in range(len(y) - 1):
        for j in range(i+1, len(y)):
            if y[i][0] > y[j][0]:
                t = y[i]
                y[i] = y[j]
                y[j] = t
    course.append(y[0])
    starting_point.append(y[0][2])
    y = []
    sum_dist += y[0][0]
    break

print(sum_dist)



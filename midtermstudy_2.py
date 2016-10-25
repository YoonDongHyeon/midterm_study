tree = {
    'O': {'A': 2, 'C': 4, 'B': 5},
    'A': {'O': 2, 'B': 2, 'D': 7},
    'B': {'O': 5, 'A': 2, 'C': 1, 'D':4, 'E':3},
    'C': {'O': 4, 'B': 1, 'E': 4},
    'D': {'B': 4, 'E': 1, 'T':5},
    'E': {'B': 3, 'D': 1, 'T': 7},
    'T': {'D': 5, 'E': 7}
}
Y=[]
ans=[]
starting_point=['O']
sum_ans = 0
while True:
    for i in starting_point:
        for j in tree[i]:
            if not j in starting_point:
                Y.append([tree[i][j], i, j])
    print("후보군:", Y)
    for i in range(len(Y) - 1):
        for j in range(i+1, len(Y)):
            if Y[i][0] > Y[j][0]:
                # Y의 i번째 인덱스의 0번째 인덱스는 숫자가 되고 그거를 비교한 거임.
                t = Y[i]
                Y[i] = Y[j]
                Y[j] = t
    ans.append(['{} 부터 {} 까지 거리는 {}'.format(Y[0][1],Y[0][2],Y[0][0])])


    sum_ans += Y[0][0]

    starting_point.append(Y[0][2])
    Y=[]
    print("완성된 경로들",ans)
    print("완료점",starting_point)
    print("-"*50)
    if len(starting_point)==len(tree):
        break
print('도로계획에 필요한 비용은',sum_ans)

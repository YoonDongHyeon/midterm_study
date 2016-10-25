load = {
    'O': {'A': 2, 'B': 5, 'C': 4},
    'A': {'O': 2, 'B': 2, 'D': 7},
    'B': {'O': 5, 'A': 2, 'C':1, 'D': 4, 'E':3},
    'C': {'O': 4, 'B': 1, 'E': 4},
    'D': {'A': 7, 'B': 4, 'E':1, 'T':5},
    'E': {'B': 3, 'D': 1, 'T': 7, 'C' : 4},
    'T': {'D': 5, 'E': 7}
}

candidate =[]
x= {
     'O': 0,
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'T': 0
    }
solved_node= ["O"]
while True:
    for i in solved_node:
        for j in load[i]:
            if not j in solved_node:
                candidate.append([load[i][j]+x[i],i,j])
    for i in range(len(candidate)-1):
        for j in range(i+1,len(candidate)):
            if candidate[i][0]>candidate[j][0] :
                t=candidate[i]
                candidate[i]=candidate[j]
                candidate[j]=t
    x[candidate[0][2]]+=candidate[0][0]
    solved_node.append(candidate[0][2])
    candidate=[]
    print(solved_node)
    print(x)
    if x["T"] >0 :
        break
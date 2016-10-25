import copy


departure = '공원입구'
destination = '전망대'
print("-----------[", departure, "->", destination, "]----------")

landscape = {
    '공원입구': {'A': 2, 'B': 5, 'C': 4},
    'A': {'공원입구': 2, 'B': 2, 'D': 7},
    'C': {'공원입구': 4, 'B': 1, 'E': 4,},
    'B': {'공원입구': 5, 'C': 1, 'A': 2, 'D': 4, 'E':3},
    'E': {'C': 4, 'B': 3, 'D': 1,'전망대': 7},
    'D': {'A': 7, 'B': 4, 'E': 1, '전망대': 5},
    '전망대': {'D': 5, 'E': 7}
}

routing = {}
for place in landscape.keys():
    routing[place] = {'shortestDist': 0, 'route': [], 'visited': 0}




def visitPlace(visit):
    routing[visit]['visited'] = 1
    for toGo, betweenDist in landscape[visit].items():
        toDist = routing[visit]['shortestDist'] + betweenDist
        if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
            routing[toGo]['shortestDist'] = toDist
            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
            routing[toGo]['route'].append(visit)
#② 집과 직접 길로 이어진 건물들까지의 최단 거리는 지도에 표시된 값으로 적고 그렇지 않은 건물들은 빈 칸으로 놓아둔다. 여기서 빈 칸의 값은 무한대를 뜻한다.

visitPlace(departure)


while True:

    minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
    toVisit = ''
    for name, search in routing.items():
        if 0 < search['shortestDist'] <= minDist and not search['visited']:
            minDist = search['shortestDist']
            toVisit = name

    if toVisit == '':
        break

    visitPlace(toVisit)

    print("[" + toVisit + "]")
    print("Dist :", minDist)

print("\n", "[", departure, "->", destination, "]")
print("Route : ", routing[destination]['route'])
print("ShortestDistance : ", routing[destination]['shortestDist'])
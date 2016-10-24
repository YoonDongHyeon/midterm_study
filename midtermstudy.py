# n = int(input('Number? : '))
# k = []
# for i in range(0,n+1):
#         print(i)
# for a in range(0, n+1):
#     k.append(a)
# yes = int(sum(k,0.0))
# print(yes)
# score = int(input('What is your score? :'))
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score <80:
#     print('C')
# elif 60 <= score <70:
#     print('D')
# else:
#     print('Fail')
# while True:
#  i = int(input('First'))
#  j = int(input('Second'))
#  k = int(input('Third'))
#  a = 0
#  if i>100 or j>100 or k>100:
#      continue
#  elif i<0 or j<0 or k<0:
#      continue
#  elif i==j or j==k or i==k:
#      continue
#  else:
#      break
# if i<j:
#     if j<k:
#         print(j)
#     elif k>j:
#         if i<k:
#             print(i)
#         else:
#             print(k)
#
# elif i>j:
#     if i<k:
#         print(i)
#     elif i>k:
#         if k>j:
#             print(k)
#         else:
#             print(j
# from __future__ import division
# from numpy import *
#
#
# class Tableau:
#     def __init__(self, obj):
#         self.obj = [1] + obj
#         self.rows = []
#         self.cons = []
#
#     def add_constraint(self, expression, value):
#         self.rows.append([0] + expression)
#         self.cons.append(value)
#
#     def _pivot_column(self):
#         low = 0
#         idx = 0
#         for i in range(1, len(self.obj) - 1):
#             if self.obj[i] < low:
#                 low = self.obj[i]
#                 idx = i
#         if idx == 0: return -1
#         return idx
#
#     def _pivot_row(self, col):
#         rhs = [self.rows[i][-1] for i in range(len(self.rows))]
#         lhs = [self.rows[i][col] for i in range(len(self.rows))]
#         ratio = []
#         for i in range(len(rhs)):
#             if lhs[i] == 0:
#                 ratio.append(99999999 * abs(max(rhs)))
#                 continue
#             ratio.append(rhs[i] / lhs[i])
#         return argmin(ratio)
#
#     def display(self):
#         print
#         '\n', matrix([self.obj] + self.rows)
#
#     def _pivot(self, row, col):
#         e = self.rows[row][col]
#         self.rows[row] /= e
#         for r in range(len(self.rows)):
#             if r == row: continue
#             self.rows[r] = self.rows[r] - self.rows[r][col] * self.rows[row]
#         self.obj = self.obj - self.obj[col] * self.rows[row]
#
#     def _check(self):
#         if min(self.obj[1:-1]) >= 0: return 1
#         return 0
#
#     def solve(self):
#
#         build full tableau
        # for i in range(len(self.rows)):
        #     self.obj += [0]
        #     ident = [0 for r in range(len(self.rows))]
        #     ident[i] = 1
        #     self.rows[i] += ident + [self.cons[i]]
        #     self.rows[i] = list(self.rows[i], dtype=float)
        # self.obj = list(self.obj + [0], dtype=float)
        #
        # solve
        # self.display()
        # while not self._check():
        #     c = self._pivot_column()
        #     r = self._pivot_row(c)
        #     self._pivot(r, c)
        #     print('\npivot column: %s\npivot row: %s' % (c + 1, r + 2))
        #     self.display()
#
#
# if __name__ == '__main__':
#     """
#     max z = 2x + 3y + 2z
#     st
#     2x + y + z <= 4
#     x + 2y + z <= 7
#     z          <= 5
#     x,y,z >= 0
#     """
#
#     t = Tableau([-2, -3, -2])
#     t.add_constraint([2, 1, 1], 4)
#     t.add_constraint([1, 2, 1], 7)
#     t.add_constraint([0, 0, 1], 5)
#     t.solve()


# 버블 정렬
# a = list(input('What is number? :'))
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             t = a[i]
#             a[i] = a[j]
#             a[j] = t
#
# print(a)

# n = int(input('사람은 몇명입니까? : '))
# b = []
# for i in range(0,n):
#     a = int(input('사람 들의 속도는 {}번째 사람'.format(i+1)))
#     b.append(a)
# for k in range(len(b)-1):
#     for j in range(k+1,len(b)):
#         if b[k] > b[j]:
#             t = b[k]
#             b[k] = b[j]
#             b[j] = t
#
# print(b)
#
# min_time = b[0] + 3*b[1] + b[3]
# print(min_time)
# 최단경로 알고리즘
# reference : http://navercast.naver.com/contents.nhn?rid=2871&contents_id=85293
# import copy
#
#
# departure = 'home'
# destination = 'school'
# print("-----------[", departure, "->", destination, "]----------")
#
# landscape = {
#     'home': {'hairShop': 5, 'superMarket': 10, 'EnglishAcademy': 9},
#     'hairShop': {'home': 5, 'superMarket': 3, 'bank': 11},
#     'superMarket': {'hairShop': 3, 'home': 10, 'EnglishAcademy': 7, 'restourant': 3},
#     'EnglishAcademy': {'home': 9, 'superMarket': 7, 'school': 12},
#     'restourant': {'superMarket': 3, 'bank': 4},
#     'bank': {'hairShop': 11, 'restourant': 4, 'EnglishAcademy': 7, 'school': 2},
#     'school': {'bank': 2, 'EnglishAcademy': 12}
# }
#
# routing = {}
# for place in landscape.keys():
#     routing[place] = {'shortestDist': 0, 'route': [], 'visited': 0}
#
#
#
#
# def visitPlace(visit):
#     routing[visit]['visited'] = 1
#     for toGo, betweenDist in landscape[visit].items():
#         toDist = routing[visit]['shortestDist'] + betweenDist
#         if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
#             routing[toGo]['shortestDist'] = toDist
#             routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
#             routing[toGo]['route'].append(visit)
#
#
# visitPlace(departure)
#
#
# while 1:
#
#     minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
#     toVisit = ''
#     for name, search in routing.items():
#         if 0 < search['shortestDist'] <= minDist and not search['visited']:
#             minDist = search['shortestDist']
#             toVisit = name
#
#     if toVisit == '':
#         break
#
#     visitPlace(toVisit)
#
#     print("[" + toVisit + "]")
#     print("Dist :", minDist)
#
# print("\n", "[", departure, "->", destination, "]")
# print("Route : ", routing[destination]['route'])
# print("ShortestDistance : ", routing[destination]['shortestDist'])

def baseball(x, y):
    global  strike
    global  ball
    if (x - d) * (x - e) * (x - f) == 0:
        if (x - y) == 0:
            strike += 1
        else:
            ball += 1
import random
a=random.randint(0,9)

while True:
    b=random.randint(0,9)
    if a==b:
        continue
    else:
        break
while True:
    c=random.randint(0,9)
    if a==c or b==c:
        continue
    else:
        break
answer = [a,b,c]
print(answer)
count = 0
sum_strike = 0
sum_ball = 0
while True:
    strike = 0
    ball = 0

    count += 1
    j = 0
    # attack= []
    # hund = int(input("Enter 백의자리 : "))
    # ten = int(input("Enter 십의자리 : "))
    # one = int(input("Enter 일의자리 : "))
    # guess = [hund,ten,one]
    try:
        guess = int(input("맞춰보세요! :"))
    except:
        print("숫자만 입력하세요")
        continue

    if guess > 999 or guess < 100:
        print("세자리 숫자로 입력하세요")
        continue

    d = (guess//100)
    e = ((guess//10)%10)
    f = (guess%10)
    if d==e or e==f or d==f:
        print('같은 숫자는쓰면 안됩니다.')
        continue
    # attack = [d,e,f]
    # print(attack)


    baseball(a,d)
    baseball(b,e)
    baseball(c,f)

    # for i in range(0, 3):
    #     if attack[i]== answer[i]:
    #         strike+=1
    print('strike is:',strike)
    #
    # for i in range(0,3):
    #     for j in range(0,3):
    #         if attack[i]==answer[j]:
    #             ball+=1
    # realball = ball - strike

    print('ball is:', ball)
    sum_strike += strike
    sum_ball += ball
    if strike !=3:
        continue
    else:
        break

print('You are Correct by {0:.2f} times'.format(count))
print('average of strike is {0:.2f}'.format(sum_strike/count))
print('average of ball is {0:.2f}'.format(sum_ball/count))
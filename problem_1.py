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

count = 0
sum_strike = 0
sum_ball = 0

while True:
    strike = 0
    ball = 0

    count += 1
    j = 0

    try:
        guess = int(input("맞춰보세요! :"))
    except:
        print("숫자만 입력하세요")
        count = 0
        continue

    if guess > 999 or guess < 100:
        print("세자리 숫자로 입력하세요")
        count = 0
        continue

    d = (guess//100)
    e = ((guess//10)%10)
    f = (guess%10)

    if d==e or e==f or d==f:
        print('같은 숫자는쓰면 안됩니다.')
        count = 0
        continue

    baseball(a,d)
    baseball(b,e)
    baseball(c,f)

    print('strike is: ',strike)
    print('ball is:' , ball)
    sum_strike += strike
    sum_ball += ball
    if strike !=3:
        continue
    else:
        print('You are Correct by {0:.2f} times'.format(count))
        print('average of strike is {0:.2f}'.format(sum_strike / count))
        print('average of ball is {0:.2f}'.format(sum_ball / count))
        break

machine_parts =[
 ['A','B''C','D','E'],
 ['1',1,0,1,0,0,0,0],
 ['2',1,1,1,1,0,0,0],
 ['3',1,1,0,0,0,0,0],
 ['4',0,0,0,1,0,0,0],
 ['5',0,0,0,0,1,1,1],
 ['6',0,0,0,0,1,1,0],
 ['7',0,0,0,0,0,1,1]]
machine_part =[
    [1,0,1,0,0,0,0],
 [1,1,1,1,0,0,0],
 [1,1,0,0,0,0,0],
 [0,0,0,1,0,0,0],
 [0,0,0,0,1,1,1],
 [0,0,0,0,1,1,0],
 [0,0,0,0,0,1,1]]
#기계 명의 제약을 없앰
# while True:
blank = [[], [], [], [], [], [], []]
changematrix = [[], [], [], [], [], [], [], []]
sum_verticalline = []
totalmatrix = [[], [], [], [], [], [], [], []]
totalmatrixsub = [[], [], [], [], [], [], [], []]
for i in range(0,7):
    for k in range(0,7):
        blank[i].append(machine_part[k][i]*(2**(k+1)))
    sum_verticalline.append(sum(blank[i]))
    # 2의 몇승을 곱해주는 작업과 그것들의 합을 구하는 과정
for i in range(0,8):
    for j in range(0,7):
        if i == 0:
            totalmatrix[i].append(sum_verticalline[j])
            totalmatrixsub[i].append(sum_verticalline[j])
        else:
            totalmatrix[i].append(machine_part[i-1][j])
            totalmatrixsub[i].append(sum_verticalline[j])
    # 확장 행렬을 써서 합을 행렬에 추가하는 작업

for k in range(0,8):
    for i in range(0,6):
        for j in range(i+1,7):
            if k == 0:
                if totalmatrix[0][i]> totalmatrix[0][j]:
                    t=totalmatrix[0][i]
                    totalmatrix[0][i]=totalmatrix[0][j]
                    totalmatrix[0][j]=t
                #         sorting 해주는 과정
            else:
                break
    # for l in range(0,7):
    #     if totalmatrix[0][l] != totalmatrixsub[0][l]:
    for k in range(1, 8):
        for i in range(0, 6):
            for j in range(1, 7):
                if totalmatrix[0][i] == totalmatrixsub[0][j]:
                    t = totalmatrix[k][i]
                    totalmatrix[k][i] = totalmatrix[k][j]
                    totalmatrix[k][j] = t
        #sorting한 확장 행렬과 sorting 하지 않은 확장행렬을 비교하여 그 위치를 알맞게 조정해주는 작업
    machine_part = [[], [], [], [], [], [], []]
        # machine_part를 초기화
    for i in range(0,7):
        for k in range(1,8):
            machine_part[i].append(totalmatrix[k][i])
        # machine_part를 행과 열을 바꾸어서 재입력
    print(machine_part)
            # continue
        # else:
        #     break
#         원래 loop로 돌려서 작업을 반복해주어야하 하지만 loop를 돌리면 오류가 나서 한번 작업하고 이것을 붙여넣기 했을 때는 정상적으로 결과가 나오는 것을 5번까지 확인하였다.
# 위의 코드를 한번 수행하는데에는 목적 기능에 이상이 없지만 loop를 쓰면 이상이 생기기에 loop를 빼고 그 내부 함수만 코드로 작성하였다.
print(totalmatrix)
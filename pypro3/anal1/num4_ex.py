# * numpy의 array() 관련 연습문제 *
import numpy as np

# 1) step1 : array 관련 문제
#  정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
# < 출력 결과 예시>
# 1행 합계   : 0.8621332497162859
# 1행 최댓값 : 0.3422690004932227
# 2행 합계   : -1.5039264306910727
# 2행 최댓값 : 0.44626169669315
# 3행 합계   : 2.2852559938172514
# 3행 최댓값 : 1.5507574553572447

data = np.random.randn(5, 4)
print(data)
print()
i = 1
for r in data:
    print(str(i) + '행 합계:', r.sum())   # np.sum(r)
    print(str(i) + '행 최대값:', r.max())
    i += 1

print()
print()

# 2) step2 : indexing 관련문제
#  문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
arr = np.zeros((6, 6))
print(arr)

#    조건1> 36개의 셀에 1~36까지 정수 채우기
cnt = 0
for i in range(6):
    for j in range(6):
        cnt += 1
        arr[i, j] = cnt
print(arr)
        
#    조건2> 2번째 행 전체 원소 출력하기 
#               출력 결과 : [ 7.   8.   9.  10.  11.  12.]
print(arr[1, :])

#    조건3> 5번째 열 전체 원소 출력하기
#               출력결과 : [ 5. 11. 17. 23. 29. 35.]
print(arr[:, 4])

#    조건4> 15~29 까지 아래 처럼 출력하기
#               출력결과 : 
#               [[15.  16.  17.]
#               [21.  22.  23]
#               [27.  28.  29.]]
print(arr[2:5, 2:5])


#  문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
#      조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
#      조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
# <<출력 예시>>
# 1. zero 다차원 배열 객체
#   [[ 0.  0.  0.  0.]
#         ...
#    [ 0.  0.  0.  0.]]
arr = np.zeros([6, 4])
print(arr)

# 2. 난수 정수 발생
# random.randint(s, e, n)
ran = np.random.randint(20, 100, 6)
print(ran)

# 3. zero 다차원 배열에 난수 정수 초기화 결과. 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# [[  90.   91.   92.   93.]
#  [  40.   41.   42.   43.]
#  [ 100.  101.  102.  103.]
#  [  22.   23.   24.   25.]
#  [  52.   53.   54.   55.]
#  [  71.   72.   73.   74.]]

ran = list(ran)

for r in range(len(arr)):
    num = ran.pop(0)
    for c in range(len(arr[0])):
        arr[r][c] = num
        num += 1
print(arr)

# 4. 첫 번째 행에 1000, 마지막 행에 6000으로 수정
#  [[ 1000.  1000.  1000.  1000.]
#   [   40.    41.    42.    43.]
#   [  100.   101.   102.   103.]
#   [   22.    23.    24.    25.]
#   [   52.    53.    54.    55.]
#   [ 6000.  6000.  6000.  6000.]]
arr[0][:] = 1000
arr[-1][:] = 6000
print(arr)

# 3) step3 : unifunc 관련문제
#   표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
#   아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
#   배열 요소의 누적합을 출력하시오.
arr = np.random.rand(4, 5)
print(arr)

# <<출력 예시>>
# ~ 4행 5열 다차원 배열 ~
# [[ 0.56886895  2.27871787 -0.20665035 -1.67593523 -0.54286047]
#            ...
#  [ 0.05807754  0.63466469 -0.90317403  0.11848534  1.26334224]]
#
# ~ 출력 결과 ~
print('평균 :', arr.mean())  # np.mean(arr)
print('합계 :', arr.sum())
print('표준편차 :', arr.std())
print('분산 :', arr.var())
print('최댓값 :', arr.max())
print('최솟값 :', arr.min())
print('1사분위 수 :', np.percentile(arr, 25))
print('2사분위 수 :', np.percentile(arr, 50))
print('3사분위 수 :', np.percentile(arr, 75))
print('요소값 누적합 :', np.cumsum(arr))

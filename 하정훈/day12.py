### 나누어 떨어지는 숫자 배열 ###
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, 
# solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.
# 입출력 예
# arr	divisor	return
# [5, 9, 7, 10]	5	[5, 10]
# [2, 36, 1, 3]	1	[1, 2, 3, 36]
# [3,2,6]	10	[-1]
# 입출력 예 설명
# 입출력 예#1
# arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

# 입출력 예#2
# arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

# 입출력 예#3
# 3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.\

def solution(arr, divisor):
    lst = []
    arr.sort()
    for i in arr:
        if i%divisor==0:
            lst.append(i)
    print(lst)

    if len(lst)!=0: 
        return lst 
    else:
        return [-1]
    

# 다른 풀이


2
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


3
4
5
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]

### 같은 숫자는 싫어 ###
# 문제 설명
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 
# 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
# 입출력 예
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]
# 입출력 예 설명

def solution(arr):
    lst = []
    for i in range(len(arr)):
        if i == 0:
            lst.append(arr[i])
        elif arr[i] != arr[i-1]:
            lst.append(arr[i])

    return lst

# 다른 풀이

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
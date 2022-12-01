# 프린터

priorities = [2, 1, 3, 2]
location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0


def solution(priorities, location):

    idx = [i for i in range(len(priorities))]
    prior = priorities.copy()
    sort_prior = sorted(prior, reverse=True)

    # print(idx)
    # print(prior)

    i = 0
    while True:
        # print(f'max(prior[{i}+1:]) = {max(prior[i+1:])}')
        if prior[i] < max(prior[i+1:]):
            idx.append(idx.pop(i))
            prior.append(prior.pop(i))
        else:
            i += 1

        if prior == sort_prior:
            break
    return idx.index(location) + 1

print(solution(priorities, location))

# https://eda-ai-lab.tistory.com/461


'''
def solution(priorities, location):
    answer = 0

    n_p = []
    
    for i in range(len(priorities)):
        n_p.append([i, priorities[i]])

    sorted_np = sorted(n_p, key=lambda x: x[1], reverse=True)
    print(n_p)
    print(sorted_np)
    
    for i in range(len(sorted_np)):
        if sorted_np[i][0] == location:
            answer = i+1
            break

    return answer

print(solution(priorities, location))
'''
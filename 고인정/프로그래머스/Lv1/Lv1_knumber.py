# k번째수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	


def solution(array, commands):
    answer = []
    for command in commands:
        print(f'command = {command}')
        new_array = array[command[0]-1:command[1]]
        print(f'command[0] = {command[0]}')
        print(f'command[0]-1 = {command[0]-1}')
        print(f'command[1] = {command[1]}')
        print(f'new_array = {new_array}')

        new_array.sort()
        print(f'new_array = {new_array}')
        answer.append(new_array[command[2]-1])
    return answer

print(solution(array, commands))
# 완주하지 못한 선수

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    # participant : 참가자, completion : 완주자, return : 미완주자
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        print(f'p, c = {p, c}')
        if p != c:
            return p
        print(p)
        print(f'completion = {completion}')
        print(f'participant = {participant}')
        print(f'participant[-1] = {participant[-1]}')
    return participant[-1]

print(solution(participant, completion))
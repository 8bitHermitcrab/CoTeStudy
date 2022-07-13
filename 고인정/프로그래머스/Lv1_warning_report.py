# 신고 결과 받기

id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    # 중복 제거
    report = list(set(report))
    # 유저가 신고한 ID
    reportID_dict = defaultdict(set)
    # 정지된 ID
    warnID_cnt = defaultdict(int)

    for i in report:
        # 신고한 ID, 신고된 ID
        reportID, warnID = i.split()
        reportID_dict[reportID].add(warnID)
        warnID_cnt[warnID] += 1

    for i in id_list:
        cnt = 0
        print(f'i = {i}')
        for j in reportID_dict[i]:
            print(f'j = {j}')
            print(f'reportID_dict[{i}] = {reportID_dict[i]}')
            if warnID_cnt[j] >= k:
                print(f'warnID_cnt[{j}] = {warnID_cnt}')
                cnt += 1
        answer.append(cnt)
        print(f'reportID_dict = {reportID_dict}')
        print(f'warnID_cnt = {warnID_cnt}')
    return answer



print(solution(id_list, report, k))


# https://velog.io/@stella317/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%8B%A0%EA%B3%A0-%EA%B2%B0%EA%B3%BC-%EB%B0%9B%EA%B8%B0Python


'''
    # 중복 제거
    report = set(report)
    report_list = []
    # 신고한 ID
    reportID_dict = {}
    # 정지된 ID 리스트
    stopID_list = []
    # 정지된 ID 개수 세기
    warnID_dict = {}
    
    for i in report:
        reporter, warner = i.split()
        
        try: reportID_dict[reporter] += warner + '/'
        except: reportID_dict[reporter] = warner + '/'
        # {'apeach': 'muzi/frodo/', 'muzi': 'frodo/neo/', 'frodo': 'neo/'}

        try: warnID_dict[warner] += 1
        except: warnID_dict[warner] = 1

    for key, value in warnID_dict.items():
        if value >= k:
            stopID_list.append(key)
            # ['frodo', 'neo']

    for key, value in reportID_dict.items():
        value = value.rstrip('/')
        v = value.split('/')
        print(v)
        report_list.append([key, v])

    for i in range(len(report_list)):
        cnt = 0
        for j in id_list:
            idx = 0
            if j == report_list[i][0]:
                for s in stopID_list:
                    if s in report_list[i][1]:
                        cnt += 1
            else:
                continue
            idx += 1

            answer.insert(idx, cnt)


    return answer'''



# for i in id_list:
    #     if i not in reporter_dict.keys():
    #         reporter_dict[i] = 0

        # for key, value in warner_dict.items():
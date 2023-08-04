def solution(id_list, report, k):

    new_report = []
    for i in report:
        new_report += [i.split(' ')]
    
    dictResult = dict.fromkeys(id_list, 0)

    for i in dictResult:
        for j in new_report:
            if (new_report.count(j) > 1):
                dictResult[j[-1]] = 1
                continue

            if (i == j[-1]):
                dictResult[i] += 1


    reportedID = []
    
    for i in dictResult.keys():
        for j in new_report:
            if dictResult[i] >= k:
                if (j[-1] == i):
                    reportedID += [j[0]]

    answer = []

    for i in dictResult.keys():
        answer += [reportedID.count(i)]

    return answer



print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2
))

print(solution(["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
))
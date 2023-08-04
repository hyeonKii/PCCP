import collections

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    reportedID = collections.defaultdict(int)

    for i in report:
        a, b = i.split(' ')
        reportHash[a].add(b)
        reportedID[b] += 1

    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if reportedID[user] >= k:
                mail += 1
        answer.append(mail)

    return reportHash, answer





print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2
))
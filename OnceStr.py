
# 한번만 등장하는 문자를 출력하는 것
# 한번만 등장하는 문자가 여러가 존재한다면 정렬할 것

# def solution(s):
#     ans = []
#     for i in s:
#         if (s.count(i) > 1):
#             continue
#         ans.append(s[s.index(i)])
#     ans.sort()    
#     res = ''.join(ans)
#     return res


def solution(s):
    answer = [i for i in s if s.count(i) == 1]
    return ''.join(answer)

print(solution('abcabcadc'))

print(solution('hello'))
# def solution(my_string):
#     ans = []
#     for i in my_string:
#         if (i in ans):
#             continue
#         ans.append(my_string[my_string.index(i)])
#     res = ''.join(ans)
#     return res

# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer += i
#     return answer



# def solution(my_string):
#     answer  = ''.join(dict.fromkeys(my_string))
#     return answer


def solution(my_string):
    answer = ''
    for i in my_string:
        if (i in set(my_string) and i not in answer):
            answer += i
    return answer


print(solution('people'))
print(solution("We are the world"))
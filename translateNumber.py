# def solution(s):
#     dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in dict:
#         if (i in s):
#             s = s.replace(i, str(dict.index(i)))    
#     return s

def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for key, value in enumerate(arr):
            s = s.replace(value, str(key))
    return int(s)

print(solution('one4seveneight'))




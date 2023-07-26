#1
# def solution(s):
#     dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in dict:
#         if (i in s):
#             s = s.replace(i, str(dict.index(i)))    
#     return s

#2
# def solution(s):
#     arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for key, value in enumerate(arr):
#             s = s.replace(value, str(key))
#     return int(s)

#3
def solution(s):
    dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    for k, v in dict.items():
        s = s.replace(v, k)
    return int(s)

print(solution('one4seveneight'))




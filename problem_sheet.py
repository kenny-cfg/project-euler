# 4. First unique character
# Given an input string, find the first non-repeating character

def solution(source):
    for x in source:
        if source.count(x) == 1:
            return x
    return None


if __name__ == '__main__':
    answer = solution('aabccbdcbe')
    print(answer)
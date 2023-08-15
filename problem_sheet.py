# 4. First unique character
# Given an input string, find the first non-repeating character

def solution(source):
    for x in source:
        if source.count(x) == 1:
            return x
    return None


def solution_with_comprehension(source):
    return [y for y in source if source.count(y) == 1][0]


if __name__ == '__main__':
    answer = solution('aaa')
    print(answer)
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    if number < 0:
        return 0
    return sum([x for x in range(3, number) if (x % 3 == 0) or (x % 5 == 0)])

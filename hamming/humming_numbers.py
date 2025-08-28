# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

def hamming(n):
    nums = [1]
    i2 = i3 = i5 = 0
    
    while len(nums) < n:
        next2 = nums[i2] * 2
        next3 = nums[i3] * 3
        next5 = nums[i5] * 5

        next_num = min(next2, next3, next5)
        nums.append(next_num)

        if next_num == next2:
            i2 += 1
        if next_num == next3:
            i3 += 1
        if next_num == next5:
            i5 += 1

    return max(nums)

# Community Solution
# def hamming(n):
#     bases = [2, 3, 5]
#     expos = [0, 0, 0]
#     hamms = [1]
#     for _ in range(1, n):
#         next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
#         next_hamm = min(next_hamms)
#         hamms.append(next_hamm)
#         for i in range(3):
#             expos[i] += int(next_hamms[i] == next_hamm)
#     return hamms[-1]

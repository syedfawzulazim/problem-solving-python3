def longestConsecutive (nums):
    sets = set(nums)
    print(sets)

    result = 0
    for num in sets:
        currentCount = 1
        if num - 1 not in sets:
            n = num
            while n + 1 in sets:
                currentCount += 1
                n += 1
        result = max(result, currentCount)
    return result


result = longestConsecutive([100,4,200,1,3,2,4])  
print(result)



# def longestConsecutive (nums):
#     if len(nums) == 0:
#         return 0
#     s = sorted(set(nums))
#     if len(nums) == 1:
#         return 1
#     print(s)
#     maxCon = 0
#     crntCon = 1
#     for i in range(len(s) - 1):
#         if abs(s[i+1] - s[i]) == 1:
#             crntCon += 1
#             #print(crntCon)
#             if i == len(s) - 2 and maxCon < crntCon:
#                 maxCon = crntCon
#         else:
#             if maxCon < crntCon:
#                 maxCon = crntCon
#             crntCon = 1
        
#     return maxCon





# result = longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])  
# print(result)
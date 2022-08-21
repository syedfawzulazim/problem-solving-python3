def twoSum( numbers, target):
    p1 = 0
    p2 = len(numbers) -1 
    while p1 <= p2:
        sum = numbers[p1] + numbers[p2]
        if sum == target:
            return [p1 + 1, p2 +1]
        elif sum > target:
            p2 -= 1
        else:
            p1 += 1
        
    


print(twoSum([2,7,10,13,15], 9))

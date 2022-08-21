def isPalindrome(st: str) -> bool:
    s = ''.join(filter(str.isalnum, st)).lower()
    length = len(s)
    if length == 0:
        return True
    p1 = 0
    p2 = length - 1
    while p1 <= p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True






s = isPalindrome(" ")
print(s)
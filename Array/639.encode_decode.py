import re
from tkinter import W


def encode(strs):
        text = ""
        for x in strs:
                text += str(len(x)) + "#" + x
        return text

def decode(strs):
        lst = []
        i = 0
        while i < len(strs):
                j = i
                while strs[j] != "#":
                        j += 1
                length = int(strs[i:j])
                print(length)
                lst.append(strs[j+1: j + 1 + length])
                i = j + 1 + length
        return lst 
        




encoded = encode(["bm", "kaku", "Kaki"])
print(encoded)
decoded =  decode(encoded)
print(decoded)
#print(decoded)


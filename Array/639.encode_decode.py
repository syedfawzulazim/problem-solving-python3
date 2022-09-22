from numbers import Number
import re
from tkinter import W


def encode(strs):
        text = ""
        for x in strs:
                text += str(len(x)) + "#" + x
        return text

def decode1(strs):
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
        

def decode(strs):
        hashfound = False
        num = ""
        r = 0
        l = 0
        res = []
        while r < len(strs):
                if strs[r] == "#":
                        num = strs[l:r]
                        res.append(strs[r+1: r+1+int(num)])
                        l = r + 1 + int(num)
                        r = l
                else:
                        r += 1
                
        print(res)

encoded = encode(["bm", "kaku", "Kaki"])
print(encoded)
decoded =  decode(encoded)
print(decoded)
#print(decoded)


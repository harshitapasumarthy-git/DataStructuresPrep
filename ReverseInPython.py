givenString = "Harshita"

def reverse(givenString):
    res =""
    for i in range(len(givenString)-1, -1 ,-1):
        res = res+givenString[i]
        i=i-1
    return res

def revFn(givenString):
    return reversed(givenString)
rev=reverse(givenString)
revF= revFn(givenString)
print(rev)
print(revF)
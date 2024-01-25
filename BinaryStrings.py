def Consecutive (s):
    primeraMitad = s[0: int (len (s)//2)]
    segundaMitad = s[int (len (s)//2): ]
    if ('0' in primeraMitad and '0' in segundaMitad) or ('1' in primeraMitad and '1' in segundaMitad):
        return False 
    return True 
        
def EqualZero (s):
    zeroes = 0
    ones = 0

    for i in range(len(s)):
        if s[i] == '0':
            zeroes += 1
        else:
            ones += 1

    return zeroes == ones 

def getSubStrings (s):
    res = []
    n = len(s)
    res = [s[i-1: j] for i in range(1, n)
          for j in range(i + 1, n + 1)]
    return res      


def cleanSubStrings(l):
    copy = [] 
    for i in l:
        if (Consecutive(i) and EqualZero(i) and len(i) % 2 == 0):
            copy.append(i) 

    return copy

def main():
    test = []
    cases = int (input())
    for i in range(cases):
        test.append(input())
    for i in range(cases):
        print (len(cleanSubStrings (getSubStrings(test[i]))))

main()
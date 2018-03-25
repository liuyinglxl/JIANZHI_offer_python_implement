def nprint(n):
    p = '0'*n
    t = '9'*n

    while p != t:
        p = list(p)
        end = 1

        while end <= n:
            if p[-end] == '9':
                p[-end] = '0'
            else:
                p[-end] = chr(ord(p[-end]) + 1)
                break
            end += 1

        p = ''.join(p)
        printNumber(p)

def printNumber(number):
    isBeginning0 = True 
    nLength = len(number)

    tmp_str = ""
    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            tmp_str += number[i]
    if tmp_str and tmp_str != None:
        print(tmp_str)

nprint(2)
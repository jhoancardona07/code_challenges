
def numberOf(n):
    count=0
    while(n!=1):
        if(n%2!=0):
            n=(3*n)+1
        else:
            n=n/2
        count=count+1
    count=count+1
    return count

def findMax(lex, rex):
    max=0
    for number in range(lex, rex+1):
        cycleLength=numberOf(number)
        if(cycleLength>max):
            max=cycleLength
    return max


n1=int(input())
n2=int(input())
print(n1, n2, findMax(n1, n2))

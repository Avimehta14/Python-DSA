#generating prime numbers upto N using SIEVE theorem
# in T.C --> O(n*log(log(n)))

from math import *

def genprimes(n):
    prime =[True]*(n+1)
    prime[0]==False
    prime[1]==False
    for p in range(2, int(sqrt(n))+1):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]= False

    for i in range(0,len(prime)):
        if prime[i]== True:
            print(i,end=" ")

print("ENTER number of numbers")
t = int(input())
genprimes(t)            


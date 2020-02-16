#!/usr/bin/python3

from math import sqrt, floor


def getPrimes():
    i = 0
    primes = []
    while i < floor(sqrt(num)):
        prime = numList.pop(0)
        primes.append(prime)
        if prime**2 > num:
            break
        delPrimes(prime)
        i += 1
    finalList = primes + numList
    return finalList


def delPrimes(prime):
    i = 0
    val = prime**2
    while i < len(numList):
        if val in numList:
            numList.remove(val)
        i += 1
        val = prime**2 + (i * prime)
        if val > num:
            break


while True:
    try:
        num = int(input("\nProvide an integer greater than 1: "))
        if num > 1:
            break
        else:
            print("\nI said GREATER than 1... Try again!\n")
            continue
    except ValueError:
        print("\nI said: Provide an INTEGER > 1... Please try again\n")

# Generate the list of integers from 2 to the number:
numList = []
for iter in range(2, num + 1):
    numList.append(iter)

print(f'\nPrime numbers <= {num}:', getPrimes())

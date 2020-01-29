import time
from math import sqrt

primes = [1]  # 1 is excluded of being a prime number
maximumPrimeAdded = -1
restrictPrimes = True


def reset():
    global primes, maximumPrimeAdded, restrictPrimes
    primes = [1]
    maximumPrimeAdded = -1
    restrictPrimes = True


def setMaxPrimes(maximum):
    global maximumPrimeAdded
    maximumPrimeAdded = sqrt(maximum)


def setRestricted(boolean):
    global restrictPrimes
    restrictPrimes = boolean


def getDivisors(value):
    currentDivisors = 0
    for everyNumber in primes:  # Checks how many divisors a number has
        if value % everyNumber == 0:
            currentDivisors += 1
    return currentDivisors


def checkIfPrime(value):  # Checks if a number is prime
    currentDivisors = getDivisors(value)
    if currentDivisors == 1:
        global restrictPrimes, maximumPrimeAdded
        if restrictPrimes and value < maximumPrimeAdded:
            primes.append(value)
        return True
    return False


def numberOfPrimes(maximum):  # Checks how many primes are in a given range
    amountOfPrimes = 0
    setRestricted(True)
    setMaxPrimes(maximum)
    for i in range(2, maximum):
        if checkIfPrime(i):
            amountOfPrimes += 1
    reset()
    return amountOfPrimes


if __name__ == "__main__":
    maxValue = input("Maximum value: ")
    startTime = time.time()
    primeAmount = numberOfPrimes(int(maxValue))
    print(primeAmount)
    endTime = time.time()
    print(endTime - startTime)

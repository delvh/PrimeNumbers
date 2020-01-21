import time

primes = [1]  # 1 is excluded of being a prime number


def getDivisors(value):
    currentDivisors = 0
    for everyNumber in primes:  # Checks how many divisors a number has
        if value % everyNumber == 0:
            currentDivisors += 1
    return currentDivisors


def checkIfPrime(value):  # Checks if a number is prime
    currentDivisors = getDivisors(value)
    if currentDivisors == 1:
        primes.append(value)
        return True
    return False


def numberOfPrimes(maximum):  # Checks how many primes are in a given range
    amountOfPrimes = 0
    for i in range(2, maximum):
        if checkIfPrime(i):
            amountOfPrimes += 1
    return amountOfPrimes


if __name__ == "__main__":
    maxValue = input("Maximum value: ")
    startTime = time.time()
    primeAmount = numberOfPrimes(int(maxValue))
    print(primeAmount)
    endTime = time.time()
    print(endTime - startTime)

#This Python program calculates the largest prime factor of the number 600851475143 (or any number), and also returns the amount of time the program took to return the result.  

#author: @carlvlewis

#recording start time of program run by importing the time module
import time
 
#defining a custom function 'n' that will serve as variable in calculating solution (gaLargestPrimeCVL)
def gaLargestPrimeCVL(n):
 
    largest_factor = 1
 
    # filtering out all even numbers to reduce program run-time, since all even whole numbers are divisible by 2 and thus not primes. we use the while statement to perform this task so that the the computer will skip all whole numbers that return 'true' to the question of whether they are divisible by 2. if 'false', computer moves on to next function.
    while n % 2 == 0:
        largest_factor = 2
        n = n/2
 
    # now we try odd factors, adding in two while statements so that the same function will be performed repeatedly on every odd number, which we define as all numbers that are 2 numbers greater than 3 (p). 
    p = 3
    while n != 1:
        while n % p == 0:
            largest_factor = p
            n = n/p
        p += 2
 
    return largest_factor
# here we calculate the time elapsed and the number of iterations it took the program to return the correct result. we use 'range' to set the maximum number of attempted iterations to 100,000.
start = time.time()
for i in range(100000): a = gaLargestPrimeCVL(600851475143)
elapsed = (time.time() - start)

# now we ask the program to give us the answer as well as the time it took to run! yay!
print "The largest prime factor is %s returned after %s seconds." % (a, elapsed)
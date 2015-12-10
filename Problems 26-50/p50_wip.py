
def genPrimes(N):
	#build array to mark
	isComposite = [0] * N	

	primes = []

	#loop ...
	for i in range(2, N):

		if isComposite[i] == 0:
			
			# i must be a prime
			primes.append(i)

			# mark off all multipes of i starting with i^2 as composite
			for j in range(i*i, N, i):
				isComposite[j] = 1
	print("done gen primes")
	return primes		


'''Simple for loop'''
'''
N = 10**6
primes = genPrimes(N)

found = [0,0]

for i in range(len(primes)-2):
	print("currently at", i)
	total = primes[i]

	# add every prime thereafter
	for j in range(i+1, len(primes)):
		total += primes[j]
		# if biggest thus far, save it
		if total in primes[j:] and j-i > found[1]:
			found = [total, j-i+1]
			print(found)
	
print("largest", found)

# Takes too long to be practical...in the order of days...
# Also running it empty takes similarly long so something inherent
#  with using for loops for large ranges
#
# import itertools
# import time
# start = time.time()

# for i in range(N):
# 	for j in range(i+1, range(N)):
# 		pass

# elapsedTime = round( ( time.time() - start ), 3 )
# print(elapsedTime, "seconds")
'''


'''Generator - nor performance difference with for loop '''
'''
def gen_sums(nums):
	done = True
	while done:

		for i in range(len(nums)-1):
			_sum = nums[i]
			for j in range(i+1, len(nums)):
				_sum += nums[j]
				yield(_sum, j-i+1)
		yield False
		# done = False

def chk_longest(N):

	primes = genPrimes(N)
	sums = gen_sums(primes)  # generator

	foundL = 0
	s = next(sums)

	while(s):
		
		if s[0] in primes and s[1] > foundL:
			foundL = s[1]
			print(s)

		s = next(sums)
		
chk_longest(10**6)
'''



'''
12        s1						n = 2
123       s2                        n = 3
1234      s3                        n = 4
12345     s4                        n = 5
123456    s5                        n = 6
1234567   s6                        n = 7

 23       s2 - 1					n = 2
 234      s3 - 1					n = 3
 2345     s4 - 1					n = 4
 23456    s5 - 1					n = 5
 234567   s6 - 1					n = 6

  34      s3 - 1 - 2				n = 2
  345     s4 - 1 - 2				n = 3
  3456    s5 - 1 - 2				n = 4
  34567   s6 - 1 - 2				n = 5

   45     s4 - 1 - 2 - 3    		n = 2
   456    s5 - 1 - 2 - 3    		n = 3 
   4567   s6 - 1 - 2 - 3    		n = 4

    56    s5 - 1 - 2 - 3 - 4 		n = 2
    567   s6 - 1 - 2 - 3 - 4 		n = 3

     67   s6 - 1 - 2 - 3 - 4 - 5    n = 2


g1 - [s1,s2,s3,s4,s5,s6]          n = idx+2
g2 - [s - 1 for s in g1[1:]]
g3 - [s - 2 for s in g2[1:]]
g4 - [s - 3 for s in g3[1:]]
g5 - [s - 4 for s in g4[1:]]
g6 - [s - 5 for s in g5[1:]]
'''

'''
# This also takes too long...

N = 10**2
primes = genPrimes(N)

total = primes[0]
g1 = []

for i in range(1, len(primes)):
	total += primes[i]
	g1.append(total)

# find longest
found = [0,0]
for i in range(len(g1)):
	sums = []
	if i == 0:
		sums = g1
	else:
		sums = [ s - g1[i-1] for s in g1[i:] ]
	print("currently at", i)
	# check if prime and longest
	for j in range(len(sums)):
		if sums[j] in primes and j+2 > found[0]:
			found = [ j+2, sums[j] ]
			print(found)

print(found)
'''

''' Better, but still too slow
import itertools
import time
start = time.time()

n = 10**6
primes = genPrimes(n)
s_primes = set(genPrimes(n)) #speed up lookup

found = [0,0]

for i in range(len(primes)):
	print(i)
	sums = itertools.accumulate(primes[i:])

	# check if prime and longest
	#  	handling StopIteration from stackoverflow.com/a/16473009
	count = 1 
	try:
		while True:  # iteration is the bottleneck (even when nothing inside)
			n = next(sums)
			if n in s_primes and count > found[1]:
				found = [n, count]
			count += 1
	except StopIteration:
		pass

print(found)

# accumulate([1,2,3,4,5]) --> 1 3 6 10 15

elapsedTime = round( ( time.time() - start ), 3 )
print(elapsedTime, "seconds")
'''


'''
n = 10**6
primes = genPrimes(n)
s_primes = set(primes) #speed up lookup

found = [0,0]

for i in range(len(primes)):
	print(i)
	sums = itertools.accumulate(primes[i:])

	# check if prime and longest
	#  	handling StopIteration from stackoverflow.com/a/16473009
	count = 1 
	try:
		while True:  # iteration is the bottleneck (even when nothing inside)
			n = next(sums)
			if n in s_primes and count > found[1]:
				found = [n, count]
			count += 1
	except StopIteration:
		pass

print(found)

# accumulate([1,2,3,4,5]) --> 1 3 6 10 15
'''


'''
n = 10**6
primes = genPrimes(n)
s_primes = set(primes) #speed up lookup

found = [0, 0]

idx = 0

for i in iter(primes):
	print("currently at", idx)
	count = 1
	total = i

	it = iter(primes[idx+1:])

	for element in it:
		count += 1
		total += element
		if count > found[0] and total in s_primes:
			found = [count, total]
			print(found)

	idx += 1

print(found)
'''


import itertools
import time
start = time.time()

n = 10**6
primes = genPrimes(n)
s_primes = set(primes) #speed up lookup

found = [0, 0]

for i in range(len(primes)):
	print("currently at", i)

	sums = list(itertools.accumulate(primes[i:]))

	for j in range(len(sums)-1, found[0]-1, -1):

		if sums[j] > n:
			continue  #skip

		e = sums[j]
		if e in s_primes:
			found = [j+1, e]
			print(found)
			break

print(found)

elapsedTime = round( ( time.time() - start ), 3 )
print(elapsedTime, "seconds")


# [543, 997651]
# 2017.07 seconds aka 34 minute! Ha! 
#  aka revisit when learn more about Python
/////Problem 26///////////////////////////////////

// Reciprocal Cycles
// Largest set of repeating digits...

# mathcentral.uregina.ca/QQ/database/QQ.09.07/h/peter18.html
# 	- Decimal value either terminates or repeats in no more digits than
#     size of the denominator
#   - If a decimal never repeats and never terminates it cannot be expressed
#     as a ratio of two integers

# find non-terminating
	# try primes between 7..1000

from decimal import *
# docs.python.org/2/library/decimal.html

primes = [ 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 
547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 
661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 
811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
947, 953, 967, 971, 977, 983, 991, 997 ]

# check max repeating
_max = 0;
assoc = 0;

for x in range(len(primes)):

	# get num
	int = primes[x]
	getcontext().prec = int * 2   #limit number of decimal places
	num = Decimal(1) / Decimal(int)

	# convert to string
	num = str(num);
	num = num[2:]  # remove "0."

	for i in range (2, int):  # i--

		# check for repeating
		chk_1 = num[0:i]
		chk_2 = num[i:2*i]
		# print(chk_1, " -- ", chk_2)

		if(chk_1 == chk_2):
			if(i > _max):
				_max = i
				assoc = int

			# exit for loop
			break

	print(int,_max)

print("----num  ",assoc, _max,"  len-----")


/////Problem 27///////////////////////////////////

// Quadratic Primes

def genPrimes(n):
	primes = [2]

	counter = 3
	while len(primes) < n:
		isPrime = True
		for p in primes:
			if(counter % p == 0):
				isPrime = False

		if(isPrime):
			primes.append(counter)

		counter += 1

	return primes

##########

# y = x^2 - bx + c

# www.desmos.com/calculator/nu4rzkjwyn
# used Desmos to visually find,
#               b   |     c
# upper limit  61   |  1000
# lower limit   0   |     1 

candidates = []

primes = genPrimes(168)  # primes < 1000

for c in range(1, 1000 + 1):
	for b in range(61 + 1):
		array = []
		for n in range (b + 1):
			val = n**2 - b*n + c

			# check if prime
			# stackoverflow.com/a/131452
			if val in primes:
				array.append(val)
			else:
				array = []
				break     # hopefuly n-forloop
		if (len(array) > 0):
			candidates.extend( [[len(array), b*c, b, c]] )

# print(candidates)

# find longest list
max_ = 0
max_idx = 0
for i in range( len(candidates) ):
	x = candidates[i][0]
	if x > max_:
		max_ = x
		max_idx = i

print(candidates[max_idx])  #[62, 59231, 61, 971]


# print("----")

# for n in range(61 + 1):
# 	val = n**2 - 61 * n + 971
# 	print(val,n)


/////Problem 28///////////////////////////////////

// Number spiral diagonals

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13


# 5*5 + 1                          5*5 + 0
#         5*1 + 2          5*1 + 4 
#                  5*0 + 1
#         5*1 + 0          5*0 + 3
# 5*3 + 2                          5*2 + 3


# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31


# 7*6 + 1                                         7*7 + 0
#         5*4 + 1                         5*5 + 0 
#                 3*2 + 1         3*3 + 0 
#                         1*0 + 1         
#                 3*1 + 2         3*0 + 3
#         5*3 + 2                         5*2 + 3
# 7*5 + 2                    						7*4 + 3

# #####

# 7 5 3      3 5 7
# 6 4 2      3 5 7

# 7 5 3      3 5 7 
# 5 3 1      0 2 4


odds_asc = range(3,1003, 2)  # 3..1001

quad2 = 0
for n in odds_asc:
	quad2 += n**2
	quad2 += n * (n-3) + 3

odds_dec = range(1001, 1, -2)  # 1001..3

quad1 = 0
for n in odds_dec:
	quad1 += n * (n-1) + 1
	quad1 += n * (n-2) + 2

total = 1 + quad1 + quad2
print(total)


/////Problem 29///////////////////////////////////

// Distinct powers
# too Easy??
seq = []
for x in range(2,101):  #2..100
	for y in range(2,101):
		seq.append(x**y)
seq = list(set(seq))  # remove duplicates
print(len(seq))


/////Problem 30///////////////////////////////////

// Digit fifth powers

combin = range(2,10**6)  #some big number...

total = 0

for elem in combin:
	num = str(elem)
	sum_ = 0
	for d in num:
		sum_ += int(d) ** 5
	if ( str(sum_) == num ):
		total += sum_

print(total)


/////Problem 31///////////////////////////////////

// Coin sums

# p = [1,2,5,10,20,50]
# lb = [1,2]
# 1 pound = 100 pence

# How many ways can u make 2lb

import itertools   
# Udacity Design of Computer Programs Lesson1/PrblmSet#2
# first introduction to itertools...

n = 200
count = 0

# p200 = list( range(0, n+1, 200) )
p100 = list( range(0, n, 100) )
p50 = list( range(0, n, 50) )
p20 = list( range(0, n, 20) )
p10 = list( range(0, n, 10) )
p5 = list( range(0, n, 5) )
p2 = list( range(0, n, 2) )
p1 = list( range(0, n, 1) )		

combos = itertools.product( p100, p50, p20, p10, p5, p2, p1 )

for combo in combos:
	if ( sum(combo) == n):
		count += 1

print(count)
#73674 + 8

/////Problem 32///////////////////////////////////

// Pandigital products

import itertools 

s = "123456789"

l_2 = itertools.permutations(s, 2)
l_3 = itertools.permutations(s, 3)
l_4 = itertools.permutations(s, 4)

def numberify(array):
	s = ""
	for a in array:
		s += a
	return s

l_2a = []
l_3a = []

l_1a = ["1","2","3","4","5","6","7","8","9"]
l_4a = []

for e in l_2:
	b = numberify(e)
	l_2a.append(b)

for e in l_3:
	b = numberify(e)
	l_3a.append(b)

for e in l_4:
	b = numberify(e)
	l_4a.append(b)

p = itertools.product(l_2a, l_3a)
p2 = itertools.product(l_1a, l_4a)

prada = []

def thingy(x):
	for pair in x:
		product = int(pair[0]) * int(pair[1])
		if( product <= 9876 ):  # 4 digits
			dig = ["1","2","3","4","5","6","7","8","9"]
			txt = pair[0] + pair[1] + str(product)
			for i in txt:
				try:
					dig.remove(i)
				except ValueError:
					pass
			if( len(dig) == 0 ):
				prada.append(product)

thingy(p)
thingy(p2)

print(len(set(prada)))  # remove duplicates
print(sum(set(prada)))

/////Problem 33///////////////////////////////////

// Digit cancelling fractions

49   4
-- = -  yes
98   8

30   3
-- = -  no   # multiples of 10?
50   5

###########

import itertools 

nums = [
	"11","12","13","14","15","16","17","18","19",
	"21","22","23","24","25","26","27","28","29",
	"31","32","33","34","35","36","37","38","39",
	"41","42","43","44","45","46","47","48","49",
	"51","52","53","54","55","56","57","58","59",
	"61","62","63","64","65","66","67","68","69",
	"71","72","73","74","75","76","77","78","79",
	"81","82","83","84","85","86","87","88","89",
	"91","92","93","94","95","96","97","98","99",
]

stuff = []

p = itertools.product(nums, nums)

for pair in p:
	candidate = False
	v = 0
	for n in pair[0]:
		try:
			pair[1].index(n)

			candidate = True
			v = n
			
		except ValueError:
			pass

	if candidate:
		# math thing
		o1 = int(pair[0])
		o2 = int(pair[1])
		orig =  o1 / o2

		n1 = list(pair[0])
		n1.remove(v)
		n2 = list(pair[1])
		n2.remove(v)
		bla = int(n1[0]) / int(n2[0])

		if (bla == orig and o1 != o2):
			stuff.append(pair)

print(len(stuff))
print(stuff)

stuff2 = stuff[:len(stuff)//2]  #no repeats
print(stuff2)

# requested answer format #manual =P
# numer = 1 * 1 * 2 * 1 = 2
# denom = 4 * 5 * 5 * 2 = 200


/////Problem 34///////////////////////////////////

// Digit factorials

# assumptions
#   max possible 999999999  ???

facts = [1,1,2,6,24,120,720,5040,40320,362880]

found = []

for num in range(3, 362880 * 7):
	sum_d = 0
	for d in str(num):
		sum_d += facts[ int(d) ]
	if sum_d == num:
		found.append(num)

print(found)
print(sum(found))


# cheated on this one to get the upper limit
# my assumed 999,999,999 was too large
# Refered here for upper limit
#	www.mathblog.dk/project-euler-34-factorial-digits/
# When it worked looked into it more and came across
#	http://mathworld.wolfram.com/Factorion.html
#   Though tbh, still don't get how to determine upper liimt for this problem


/////Problem 35///////////////////////////////////

// Circular primes

def circulars(n):
	s = str(n)
	ln = len(s)
	c = []
	for i in range(1, ln):
		x = i
		num = ""
		while len(num) < ln:
			if( x == ln):
				x = 0
			num += s[x]
			x += 1
		c.append( int(num) )
	return c

def genPrimes(n):
	primes = [2]
	counter = 3
	while len(primes) < n:
		isPrime = True
		for p in primes:
			if( p > counter ** 0.5):
				break    # exit for loop
			if(counter % p == 0):
				isPrime = False

		if(isPrime):
			primes.append(counter)

		counter += 2  # odds

	return primes

mp = genPrimes(78498)  # how many primes less than x
					   # http://en.wikipedia.org/wiki/Prime-counting_function
mp = mp[5:]  # remove 2,3,5,7,11

circs = [2,3,5,7,11]

while (len(mp) > 0):
	p = mp[0]
	c = circulars(p)
	allTru = True
	for n in c:
		try:
			i = mp.index(n)
			del mp[i]   # avoid repeating
		except ValueError:
			allTru = False
	if(allTru):
		circs.append(p)
		circs.extend(c)
	mp.remove(p)   # avoid repeating

print(circs)
print(len(circs))


/////Problem 36///////////////////////////////////

// Double-base palindromes

def is_palindrome(s):
	ln = len(s)
	m = ln // 2
	n = m - 1
	if ln % 2 == 0 :
		if( s[:m] == s[:n:-1] ):    # stackoverflow.com/a/931095
			return True
	else:
		if( s[:m] == s[:m:-1] ):
			return True
	return False

stuff = []

for i in range(10**6):
	n = is_palindrome( str(i) )
	b = is_palindrome( '{0:b}'.format(i) )    # stackoverflow.com/a/699891
	if( n and b):
		stuff.append(i)

print(sum(stuff))
print(stuff)


/////Problem 37///////////////////////////////////

// Truncatable primes

def genPrimes(n):     #note to self... num of primes in range(N) is approx == N / ln(N) ... tho accuracy starts @ never?? http://en.wikipedia.org/wiki/Prime_number_theorem#Table_of_
	primes = [2]
	counter = 3
	while len(primes) < n:
		isPrime = True
		for p in primes:
			if( p > counter ** 0.5):
				break    # exit for loop
			if(counter % p == 0):
				isPrime = False

		if(isPrime):
			primes.append(counter)

		counter += 2  # odds

	return primes

kp = genPrimes(78498)

print("done gen primes...waiting on the rest")

fp = []  # semi-filtered

for p in kp:
	pushMe = True

	sp = str(p)
	for o in '19':   # ends or starts with
		if sp[0] == o:
			pushMe = False
		if sp[ len(sp) - 1 ] == o:
			pushMe = False
	for e in '0468':   # contains 
		try:
			sp.index(e)
			pushMe = False
		except:
			pass
	for d in range(1, len(sp)-1):
		for x in '52':   # in middle
			if sp[d] == x: 
				pushMe = False

	for d in range(len(sp)-1):
		if sp[d] == sp[d+1]:   # doubles....
			pushMe = False

	if pushMe :
		fp.append(p)

fp = fp[4:] # remove 2,3,5,7

print("semi filtered to", len(fp), "... waiting on the rest")


def check(num):
	isTP = True
	s1 = list( str(num) )    # stackoverflow.com/a/11493649

	for i in range(1, len(s1)):
		v = int ( ''.join( s1[:i] ) )
		try:
			kp.index(v)
		except ValueError:
			isTP = False

	if isTP:
		for i in range(1, len(s1)):			
			v = int ( ''.join( s1[i:] ) )
			try:
				kp.index(v)
			except ValueError:
				isTP = False
	
	if isTP:
		return True
	else:
		return False

found = []

for n in fp:
	if check(n):
		found.append(n)

print(len(found))
print(sum(found))
print(found)

/////Problem 38///////////////////////////////////

// Pandigital multiples

mult = [9] + (list(range(90, 100)) +
			  list(range(900, 1000)) +
			  list(range(9000, 10000)) +
			  list(range(90000, 100000)) +
			  list(range(900000, 1000000)) +
			  list(range(9000000, 10000000)) +
			  list(range(90000000, 100000000))  )  

# some rules for m, see if work...
#    has a 9
#	 no repeating digits
#    max 9 digits

blah = ''

for m in mult:
	s = str(m)
	st = set(s)
	if ( len(s) == len(st) ):  # non-repeating
		if( '9' in st):  # contains 9
			c = ''
			i = 1
			while i <= 9 and len(c + str(m * i)) <= 9 \
						and len(set(c)) == len(c) \
						and '0' not in set(c + str(m * i)):				
				c += str(m * i)
				i += 1
				# print(c)
			if len(set(c)) == 9:
				blah = c #[c, i, m]

print(blah)


/////Problem 39///////////////////////////////////

// Integer Right Triangles

p = []
for a in range(800):
	for b in range(800):
		c = pow( (a*a + b*b), 0.5 )
		p.append(a + b + c)

from collections import Counter  # http://stackoverflow.com/a/5829377

d = Counter(p)


sorted_d = sorted(d.items(), key = lambda x: x[1], reverse=True) # http://stackoverflow.com/a/2258273

for i in range(len(sorted_d)):
	if sorted_d[i][0] <= 1000:
		print(sorted_d[1])
		break


/////Problem 40///////////////////////////////////

// Champernowne`s constant

s = ''
c = 0
while len(s) < pow(10,6):
	c += 1
	s += str(c)

sum_ = ( 
	int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) *
	int(s[9999]) * int(s[99999]) * int(s[999999])
)

print(sum_)


/////Problem 41///////////////////////////////////

// Pandigital prime

def genPrimes2(m):  #by max prime
	primes = [2]
	counter = 3
	while counter <= m:
		isPrime = True
		for p in primes:
			if( p > counter ** 0.5):
				break    # exit for loop
			if(counter % p == 0):
				isPrime = False

		if(isPrime):
			primes.append(counter)

		counter += 2  # odds

	return primes

primes = genPrimes2( pow(10,6) )    #note to self... num of primes in range(N) is approx == N / ln(N)
print("generated primes")

def checkPrime(n):   #only as accurate as size of primes[]
	isPrime = True
	for p in primes:
		if p >= n:
			break
		elif n % p == 0:
			isPrime = False
			break
	return isPrime


from itertools import permutations

perms = []
ofInterest = ['987654321', '87654321', '7654321', '654321', '54321', '4321']

for i in ofInterest:
	perms += list( permutations(i))
perms = [ int("".join(e)) for e in perms ]   #turn strings to nums


for p in perms:
	if checkPrime(p) :
		print(p)
		break

# So elegant....
#    www.mathblog.dk/project-euler-41-pandigital-prime


////// About that prime function....  /////////////

	'''What I have atm is slow ... see checkPrime_speedTest.py & checkPrime_speedTest.py for faster
		Read through KA lessons to pick up new tricks'''

	# To generate, sieve seems fastest
	'''Sieve Division
		first builds list of primes, then does a trial divsion on primes up to the square root of N'''
		# www.khanacademy.org/cs/a/1097515635
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
			
			return primes


	# To check, Fermat's Primality test is fastest (fixed time regardless of
	# size of N)... but not 100% accurate
	'''Fast mod and Fermat's Little Theorem 
		Not 100% accurate - marks Carmichael numbers as prime '''
		# www.khanacademy.org/cs/p/level-10-fermat-primality-test
		def fastermod(A, B, C):
			result = 1
			while B > 0:
				if B % 2 == 1:   # odd
					result = (result * A) % C 	#???
					B -= 1
				B /= 2							#???	
				A = pow(A,2) % C   				#???
			return result

		def GCD(A,B):
			if A == 0 or B == 0:
				return None

			c = max(A,B)
			d = min(A,B)

			while d != 0:
				r = c % d
				c = d
				d = r

			return c

		from random import randint

		def fermatPrimalityTest(N, nTrials):
			if N % 2 == 0:
				return False

			# default nTrials of 1/2
			if nTrials == "default":
				nTrials = int(N/2)

			# test a random candidate
			for i in range(nTrials):
				r = randint(2, N-1)

				# ??
				if GCD(r,N) != 1:
					return False

				if fastermod(r,N,N) != r:
					return False   # found a witness

			return True


	# For 100% accuracy, a distant second is simple division
	'''Start from 3 to the square root of N skipping all multiples of 2'''
		# www.khanacademy.org/cs/a/1097515635
		def checkPrime(N):
			if N % 2 == 0:   # divisible by two
				return False

			for i in range(3, int(N**0.5+1), 2):
				if N % i == 0 :
					return False

			return True



/////Problem 42///////////////////////////////////

// Coded triangle numbers


from p42_words import words

alpha = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def nthTri(n):
	return 0.5*n*(n+1)

tris = [nthTri(i) for i in range(1,30)]

count = 0
for w in words:
	s = 0
	for e in w:
		s += alpha.index(e)

	if s in tris:
		count += 1
print(count)


/////Problem 43///////////////////////////////////

// Sub-string divisibility

def passes(n):

	(v1,v2,v3,v4,v5,v6,v7) = ( int( n[1] + n[2] + n[3] ),
							   int( n[2] + n[3] + n[4] ),
							   int( n[3] + n[4] + n[5] ),
							   int( n[4] + n[5] + n[6] ),
							   int( n[5] + n[6] + n[7] ),
							   int( n[6] + n[7] + n[8] ),
							   int( n[7] + n[8] + n[9] ),
							 )
	
	if v1 % 2 != 0:
		return False
	elif v2 % 3 != 0:
		return False
	elif v3 % 5 != 0:
		return False
	elif v4 % 7 != 0:
		return False
	elif v5 % 11 != 0:
		return False
	elif v6 % 13 != 0:
		return False
	elif v7 % 17 != 0:
		return False
	else:
		return True


from itertools import permutations

total = 0

for p in permutations('0123456789',10):
	n = ('').join(map(str,p))
	if passes(n):
		total += int(n)
print(total)


/////Problem 44///////////////////////////////////

// Pentagonal numbers
def genPentagonal(n):
	pNums = []
	for i in range(n,0,-1):  #descending order
		pNums.append( int(i * (3*i - 1) / 2) )
	print("done gen array")
	return pNums

N = 10000 #arbitrary large number
penNums = genPentagonal(N)

''' check against array - too slow '''
# for i in range(N):
# 	for j in range(i+1, N):
# 		n1, n2 = penNums[i], penNums[j]
# 		d = n1 - n2
# 		if d in penNums:
# 			s = n1 + n2
# 			if s in penNums:
# 				print(n1, n2, s, d)

def isPentagonal(n):
	# https://en.wikipedia.org/wiki/Pentagonal_number
	t = (24 * n + 1)**0.5
	test1 = int(t) - t == 0  #perfect square
	test2 = t % 6 == 5
	return test1 and test2

''' check against formula '''
for i in range(N):
	for j in range(i+1, N):
		n1, n2 = penNums[i], penNums[j]
		d = n1 - n2
		if isPentagonal(d):
			s = n1 + n2
			if isPentagonal(s):
				print(n1, n2, s, d)

# 7042750 1560090 8602840 5482660

/////Problem 45///////////////////////////////////

// Triangular, pentagonal, hexagonal numbers

def isPentagonal(n):
	# https://en.wikipedia.org/wiki/Pentagonal_number
	t = (24 * n + 1)**0.5
	test1 = int(t) - t == 0  #perfect square
	test2 = t % 6 == 5
	return test1 and test2

def isHexagonal(n):
	# https://en.wikipedia.org/wiki/Hexagonal_number
	t = ((8 * n + 1)**0.5 + 1)/4
	return int(t) - t == 0

def isTriangular(n):
	# https://en.wikipedia.org/wiki/Triangular_number
	t = (8 * n + 1)**0.5
	return int(t) - t == 0


N0 = 144
N1 = 100000 #arbitrary large number

for i in range(N0,N1):	
	n = i * (2*i - 1)	# gen hexagonal number
	if isPentagonal(n):
		if isTriangular(n):
			print(n)
			break


/////Problem 46///////////////////////////////////

// Goldbach''s other conjecture

''' Sieve Division - first builds list of primes, 
     then does a trial divsion on primes up to the square root of N
	 By Brit Cruise, www.khanacademy.org/cs/a/1097515635
'''
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


N = 10000 #arbitrary large number
primes = genPrimes(N)

squares = [n**2 for n in range(1, N)]

def goldbach(n):
	# check if odd composite
	if n not in primes and n % 2 != 0:
		# check if falsifies conjecture
		isRight = False
		for p in primes:
			if p > n - 2:
				break
			else:
				for s in squares:
					if p + s * 2 > n:
						break
					elif int(p + s * 2) == n:
						isRight = True
						# print(n, p, s)
						return isRight
		return isRight


for i in range(2,N):
	if goldbach(i) is False:
		print(i)
		break


/////Problem 47///////////////////////////////////

// Distinct prime factors

def distinctPrimeFactors(nums):
	primes = genPrimes( max(nums)+1 ) #largest number, generate prime list once
	ofInterest = [1,1,1]

	for n in nums:
		count = 0

		for p in primes:
			if p >= n: break

			if n % p == 0 :
				count += 1   # found a prime factor

			if count == 4: 
				# check if consecutive
				if ( n - 1 == ofInterest[-1] and
					 n - 2 == ofInterest[-2] and
					 n - 3 == ofInterest[-3]
					):
					return ofInterest[-3] # found one, exit

				else :
					ofInterest.append(n)  # add number
					ofInterest = ofInterest[1:] # keep ofInterest at min len
					break 				  # and stop checking for more pFs


# will fail for something like 2x2x3x3, but trying my luck

N = 1000000 #arbitrary large number
print( distinctPrimeFactors(list(range(N))) )


/////Problem 48///////////////////////////////////

// Self powers

#trivial??
total = 0
for n in range(1, 1001):
	total += n ** n
print(str(total)[-10:])


/////Problem 49///////////////////////////////////

// Prime permutations

#gen 4 digit primes, 1009..9973
primes = genPrimes(10000)
temp = genPrimes(1000)
primes = primes[ (len(primes)-len(temp))*-1: ] 
primes = [str(e) for e in primes] #convert items to strings

from itertools import permutations

#for each, check for all its permutations (4x3x2x1)
def findSeq():
	series = []
	for prime in primes:

		# create list of its prime permutations
		perms = permutations(prime)
		temp = []
		for perm in perms:
			p = ''.join(perm)
			if p in primes:
				temp.append(p)
				primes.remove(p)

		# look for sequential series
		if len(temp) > 2:
			temp = sorted([int(e) for e in temp])  #ascending
			# print(temp)

			# looking for seq of at least three
			for i in range(len(temp)-2):
				for j in range(i+1, len(temp)):
					d = temp[j] - temp[i]
					n3 = temp[j] + d
					if n3 in temp:
						series.append((temp[i], temp[j], n3))
	return series

print(findSeq())


/////Problem 50///////////////////////////////////

// Consecutive prime sum

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

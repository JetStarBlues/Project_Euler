
///Problem 1////////////////////////////////////

var myArray = [];

for ( var i = 0; i < 1000; i++ ){
	if ( i % 3 == 0 )
		myArray.push(i);
	else if ( i % 5 == 0 )
		myArray.push(i);
}

// get sum of elements
var sum = 0;
for ( var i = 0; i < myArray.length; i++ ){
	sum += myArray[i];
}

console.log (sum);

/////Problem2//////////////////////////////////

var fib = [1,2];

var i = 2;
var new_ = 0;
while (new_ < 4 * Math.pow(10, 6) ) {
	new_ = fib[i-1] + fib[i-2];
	fib.push( new_ );
	i++;
}

console.log (fib);

// sum of even
var sum = 0;
for ( var i = 0; i < fib.length; i++ ){
	cur = fib[i];
	if (cur % 2 == 0)
		sum += cur;
}

console.log (sum);

/////Problem3///////////////////////////////////

//prime number generator
--//Sieve of Eratosthenes (via Jamie)//--

	var max = 40;
	var primes = [];
	var nonPrimes = [];

	for (var i = 2; i < max; i++ ){   // first prime number is 2
		var cur = i;

		// check that cur is not in nonPrimes[]
		if ( nonPrimes.indexOf( cur ) < 0 ){

			// if it isn't, must be a prime
			primes.push(cur);

			// eliminate all its multiples
			for ( var x = 2; x < max; x++ ){
				var mult = cur * x;
				if (mult < max)
					nonPrimes.push( mult );
			}
		}
	}

	console.log( primes );

	// limitations, size of nonPrimes[] and time takes
	// to seek through it puts a cap

//What is the largest prime factor of the number 600851475143 ?
--// Fermat's Factorization (Wikipedia) - Basic //--
	/*
		N = a^2 - b^2  			// where N is odd
		  = (a - b) * (a + b)

		b^2 = a^2 - N
		b   = sqrt ( a^2 - N )

		max_b = Math.floor( N/2 )
		max_a = max_b + 1
	*/
// see largestPrime.js


/////Problem 4///////////////////////////////////

	//sum of squares
		//1^2 + 2^2 + ... + 10^2 = 385
	//square of sum
		//(1 + 2 + ... + 10)^2 = 552 = 3025
	//find diff
		//3025 − 385 = 2640

var squares = [];
var sum_of_squares = 0;
var sum = 0;
var square_of_sum; var sum;

for (var i = 1; i < 101; i++ ){
	sum += i;
	squares.push( Math.pow(i,2) );
}

//console.log (sum);
//console.log (squares);

for (var i = 0; i < squares.length; i++){
	sum_of_squares += squares[i];
}

square_of_sum = Math.pow(sum,2);

//console.log(sum_of_squares);
//console.log(square_of_sum);

var diff = square_of_sum - sum_of_squares;

console.log(diff);


/////Problem 5///////////////////////////////////
/*
	2520 is the smallest number that can be divided by each of the numbers 
	from 1 to 10 without any remainder.

	What's equivalent for 1 to 20?
*/
//en.wikipedia.org/wiki/Least_common_multiple#Finding_least_common_multiples_by_prime_factorization


/////Problem 6///////////////////////////////////
/*
	A palindromic number reads the same both ways.
	The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

	Find the largest made from product of two 3-digit numbers.
*/

var n = 999;
var palindromes = [];

function palindrome(second_num){
	for (var i = 999; i > 0; i--){
		var mult = second_num*i;
		var str = String(mult);
		if (str.length == 5){
			var first = str[0] + str[1];
			var second = str[4] + str[3];
		
			if (first == second){
				console.log("found one. It is " + mult);				
				//console.log("the factors are " + i + " and " + second_num);

				palindromes.push(mult);
			}
		}
		else if (str.length == 6){
			var first = str[0] + str[1] + str[2];
			var second = str[5] + str[4] + str[3];

			if (first == second){
				console.log("found one. It is " + mult);
				//console.log("the factors are " + i + " and " + second_num);

				palindromes.push(mult);
			}
		}	
	}
}

//likely in this range
for (var i = 999; i > 666; i--){
	palindrome(i);
}
//sort numerically
palindromes.sort(function(a,b){return b-a});


/////Problem 7///////////////////////////////////

// Find the 10 001st prime number

	var max = 40;

	function prime_gen(max){
		var primes = [2];	// first prime number is 2
		var nonPrimes = [];

		for (var i = 3; i < max; i +=2 ){    // check only odd #s
			var cur = i;

			// check that cur is not in nonPrimes[]
			if ( nonPrimes.indexOf( cur ) < 0 ){

				// if it isn't, must be a prime
				primes.push(cur);

				// eliminate all its multiples
				for ( var x = 2; x < max; x++ ){
					var mult = cur * x;
					if (mult < max)
						nonPrimes.push( mult );
				}
			}
		}
		console.log( "this is the " + primes.length + "st ," );
		console.log( primes[primes.length - 1] );
	}

/////Problem 8///////////////////////////////////

// Find the greatest product of five consecutive digits in the 1000-digit number

var str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

var products = [];

for (var i = 0; i < str.length - 5; i++ ){	

	var product = Number( str[i] ) *
				  Number( str[ i+1 ] ) *
				  Number( str[ i+2 ] ) *
				  Number( str[ i+3 ] ) *
				  Number( str[ i+4 ] );

	products.push(product);
}

//sort 
products.sort(function(a,b){return b-a});
//
console.log("largest product is " + products[0] );

/////Problem 9///////////////////////////////////

// a^2 + b^2 = c^2
// a + b + c = 1000
// Find the product abc

//Brute force...

function thousand_triplet (N){
	for (var x = 1; x < N; x++ ){   //ignore 0
		for (var y = 1; y < N; y++ ){
			for (var z = 1; z < N; z++ ){

				if ( (x*x + y*y) == z*z )
					if ( x + y + z == 1000 )
						console.log("found em " + x + "," + y + "," + z);
				
			}
		}
	}
}

/////Problem 10///////////////////////////////////

// find sum of all primes below 2million

//Sieve of Sundaram
//		see V3


/////Problem 11///////////////////////////////////

// greatest product of four adjacent numbers in the same direction 
// (up, down, left, right, or diagonally)

... just multiply without checking
... then compare (isNaN probably treated like zero)

//20x20
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59


 -63        -60         -57
    -42     -40      -38
       -21  -20   -19
 -3 -2 -1  idx(x) +1  +2  +3
       +19  +20   +21
    +38     +40      +42
 +57        +60         +63


/////-----

var nums = [];  //20x20

var maxes = [];

// Max function -> http://stackoverflow.com/a/1379556
function max(array){
	return Math.max.apply( Math, array );
}

for (var i = 0, l = nums.length; i < l; i++ ){
 	// calculate 8 products
 	var P1 = nums[i] * nums[i - 60] * nums[i - 40] * nums[i - 20]; 
 	var P2 = nums[i] * nums[i + 20] * nums[i + 40] * nums[i + 60];
 	var P3 = nums[i] * nums[i + 21] * nums[i + 42] * nums[i + 63];
 	var P4 = nums[i] * nums[i - 21] * nums[i - 42] * nums[i - 63]; 
 	var P5 = nums[i] * nums[i + 19] * nums[i + 38] * nums[i + 57]; 
 	var P6 = nums[i] * nums[i - 19] * nums[i - 38] * nums[i - 57]; 
 	var P7 = nums[i] * nums[i + 1] * nums[i + 2] * nums[i + 3];
 	var P8 = nums[i] * nums[i - 1] * nums[i - 2] * nums[i - 3];

 	var products = [];
 	// check NaN
 	if (P1) products.push(P1);
 	if (P2) products.push(P2);
 	if (P3) products.push(P3);
 	if (P4) products.push(P4);
 	if (P5) products.push(P5);
 	if (P6) products.push(P6);
 	if (P7) products.push(P7);
 	if (P8) products.push(P8);

 	// find max
 	var m = max(products);
 	maxes.push(m);
 }

//find largest
console.log( max(maxes) );


/////Problem 12///////////////////////////////////

//What is the sum of the digits of the number 2^1000

//Trivial

x = str( pow(2,1000) )

print(x)

total = 0

for i in x:
	total = total + int(i)

print(total)



/////Problem 13///////////////////////////////////

// Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

// Trivial

nums = []

total = 0

for i in nums:
	total = total + i

str = str( total )

x = ""

for i in range(10):
	x = x + ( str[i] )

print(x)


/////Problem 14///////////////////////////////////

// slow, but whatevs

counter = 0

def sequence(N):
	global counter

	if ( N % 2 == 0 ):    		#even
		N = N / 2
	else:						#odd
		N = 3 * N + 1

	if ( N > 1 ):
		counter += 1
		return sequence(N)						
	elif ( N == 1):
		#print("took " + str(counter) )
		return counter
	else:
		return -1    #not sure if this ever happens...

####

steps = []

for i in range(1000000):
	x = sequence(i)
	steps.append(x)
	counter = 0

#print(steps)

#find index of max
m = max(steps)
y = steps.index(m)     # get number
print( y )


/////Problem 15///////////////////////////////////

//Triangular numbers

#find all factors

def total(n):
	factors = []
	for i in range (2, int(n**0.5) + 1 ):
		if n % i == 0
			factors.extend( [i, n/i] )   # stackoverflow.com/a/16621512/2354735
	return len(factors)

def main(m):
	g = 0
	for i in range (m):
		g = g + i      			# increment to next triangle number
		if ( total(g) > 497):   # compare number of factors
			print (g)
			return

main(1000000)

/////Problem 16///////////////////////////////////

//Factorial digit sum 

# Lol, too easy..??

import math 

n = math.factorial(100)
n = str(n)
sum = 0
for i in n:
	sum = sum + int(i)
print(sum)

/////Problem 17///////////////////////////////////

//Lattice paths

#www.robertdickau.com/lattices.html

# lol, no way this could be solved with pen n paper
# answer was 137846528820

def pascalTriangle(N):
	mega = [ [1,1] ]
	for i in range(N):
		cur_row = [1]      #leading 1
		prev_row = mega[i]
		for x in range( len(prev_row) - 1):
			cur_row.append( prev_row[x] + prev_row[x+1] )
		cur_row.append(1)  #trailing 1
		mega.append(cur_row)
	print(mega)

	# get middle value (specific to this problem)
	print("---")
	mid = int ( len( mega[39] ) / 2 )
	print( mega[39][mid] )

pascalTriangle(39)

/////Problem 18///////////////////////////////////

//1000-digit fibonacci number

def fib(N):
	fibseq = [1,1]
	for i in range(N):
		fibseq.append( fibseq[i] + fibseq[i+1])
	#print (fibseq)

	#check  (specific to this problem)
		if len( str(cur) ) > 999:
			print ( i )
			return
fib(100000)

/////Problem 19///////////////////////////////////

//Number letter counts

# 1..9
	# 1..9 + ten

# 10..19
	# ten..nineteen
   
# 20..99
	# 9 * ( 1..9 + twenty..ninety ) 

====

s1_to_9 = "onetwothreefourfivesixseveneightnine"

s10_to_19 = "teneleventwelvethriteenfourteenfifteensixteenseventeeneighteennineteen"

s_ty = "twentythirtyfortyfiftysixtyseventyeightyninety"

i1_to_99 = ( len(s1_to_9) +
			 len(s10_to_19) +
			 len(s_ty) * 10 + 8 * len(s1_to_9)
			)

ands = len('and') * 99 * 9

final = ( 10 * i1_to_99 +   		# 97
		  ands +       				# and
		  900 * len('hundred') + 	# hundred
		  100 * len(s1_to_9)		# one
		)

print( final + len('onethousand') )  # 'onethousand' was the catch


/////Problem 20///////////////////////////////////

//Maximum path sum I

nums = [[75],
		[95,64],
		[17,47,82],
		[18,35,87,10],
		[20,04,82,47,65],
		[19,01,23,75,03,34],
		[88,02,77,73,07,63,67],
		[99,65,04,28,06,16,70,92],
		[41,41,26,56,83,40,80,70,33],
		[41,48,72,33,47,32,37,16,94,29],
		[53,71,44,65,25,43,91,52,97,51,14],
		[70,11,33,28,77,73,17,78,39,68,17,57],
		[91,71,52,38,17,14,91,43,58,50,27,29,48],
		[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
		[04,62,98,27,23,09,70,98,73,93,38,53,60,04,23]]

# See seperate file for solution...

#1074


/////Problem 21///////////////////////////////////

//Counting Sundays

# Step 1) gen big array

	# J  F  M  A  M  J  J  A  S  O  N  D 
	# 31 28 31 30 31 30 31 31 30 31 30 31
	# 31 28 31 30 31 30 31 31 30 31 30 31
	# 31 28 31 30 31 30 31 31 30 31 30 31
	# 31 29 31 30 31 30 31 31 30 31 30 31

# year generator

def yr_gen(leap):

	# days = [31 31 30 31 30 31 31 30 31 30 31]

	t0 = list(range(1,31))	# 30 days
	t1 = list(range(1,32))	# 31 days
	t8 = list(range(1,29))	# 28 days
	t9 = list(range(1,30)) 	# 29 days

	days = t1 * 2 + (t0 + t1) * 2 + t1 + (t0 + t1) * 2

	# insert either 28 or 29
	if leap:
		days[31:1] = t9 	# stackoverflow.com/a/7376026
	else:
		days[31:1] = t8

	return days

# print( yr_gen(True) )


meatloaf = yr_gen(False) * 4  # initialize as such since 1900 not leap

chunk = yr_gen(False) * 3 + yr_gen(True)

meatloaf += chunk * 24   

print (meatloaf)

# Step 2) check every 7th element (since Jan 1 1900 is (conviniently) a Mon)

counter = 0
for x in range(-1, len(meatloaf), 7):   # [-1, 6, 13, ..]
	if x < 0:
		pass
	if meatloaf[x] == 1:
		counter += 1

print (counter)  #171


/////Problem 22///////////////////////////////////

// Amicable numbers

def sum_f(n): 	#sum of factors

	factors = [1]
	for i in range (2, int(n**0.5) + 1 ):
		if n % i == 0:
			factors.extend( [i, n/i] ) 
	return int( sum(factors) )

def reloaded(max):
	# sum_f all numbers within range
	list_of_sums = []
	for i in range (4, max):
		pair = [] 			# format -> [ num, sumF ]
		pair.append( i )   			
		pair.append( sum_f(i) )
		if ( pair[0] != pair[1] ):	# avoid doubles ex. [28,28]
			list_of_sums.append(pair)
	#print(list_of_sums)

	# for each, see if there is a pair equivalent to self reversed
	amicable = []
	for pair in list_of_sums:
		reversed = [ pair[1], pair[0] ]
		try:
			list_of_sums.index(reversed)   # if so, 

			amicable.append( pair ) 	   # add self to amicable
			list_of_sums.remove(pair)      # and remove the reversed from list
		except ValueError:
			pass			
	#print(amicable)

	# sum up all the pairs 
	ultrasum = 0
	for pair in amicable:
		ultrasum += pair[0] + pair[1]

	print(ultrasum)

reloaded(10000)  #31626

#852810

/////Problem 23///////////////////////////////////

// Names Scores

alpha = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"

txt_file = open("names.txt", "r")

names = txt_file.read().split(',')

names.sort()

grandulous_total = 0

for i in range(len(names)):
	letter_score = 0
	for letter in names[i]:
		letter_score += alpha.index(letter)
	grandulous_total += (i + 1) * letter_score # one_based counting

print(grandulous_total)

#871198282

/////Problem 24///////////////////////////////////

// Lexicographic permutations

from itertools import permutations 

a = permutations('0123456789')
b = []

# convert to list 
for item in a:
	b.append(item)

# get millionth item 
print( b[999999] )

/////Problem 25///////////////////////////////////

// Non-abundant sums 

from itertools import combinations

def sum_f(n): 	#sum of factors [UPDATED!]

	factors = [1]
	for i in range (2, int(n**0.5) + 1 ):
		if n % i == 0:
			if ( i != n/i):
				factors.extend( [i, n/i] )
			else:
				factors.extend( [i] )  # deal with perfect squares
	return sum(factors)

def reactor(blah):

	# gen list of abundant numbers
	abundant = []
	for i in range(2, blah):
		sumF = sum_f(i)

		if(sumF > i):  # if 'abundant'
			abundant.append(i)
	print("start abundant", abundant, "end abundant")

	
	# gen list of all possible sums
	sums = []

	for i in range( len(abundant) ):
		for j in range( i, len(abundant)):
			sum_ = abundant[i] + abundant[j]
			if sum_ <= 20163: # 28123: # theoretical limit 
				sums.append(sum_)

	# remove repeating values using 'set'
	sums = sorted( set(sums) ) 
	print("start sums ", sums, "end sums")

	# find numbers not in sums[]
	foundya = []

	cur = 1
	for val in sums:
		while cur < val:
			foundya.append(cur)
			cur += 1
		cur += 1 # advance to next

	#print("start foundya", foundya, "end foundya")

	# return sum of items in foundya
	ultrasum = 0
	for item in foundya:
		ultrasum += item

	print(ultrasum)

reactor(28123)

/////Problem 26///////////////////////////////////

// Title 
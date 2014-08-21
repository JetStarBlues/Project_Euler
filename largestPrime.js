	//var N = 600851475143; //5959;
	
function largestPrime (N) {

	var a = {};
	a.val = 0;
	var b = {};
	b.val = 0, b.is_int = false;

	var prime_factors = [];
	var first_168 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997];
	
	var max_b = Math.floor ( N / 2 );
	//var max_a = max_b + 1;

	var init_a = Math.ceil( Math.pow ( N, 0.5 ) );	//round_up

	a.val = init_a;   // initialize
		console.log(a);

	// first check if even
	/*
		var is_even;
		if ( N % 2 == 0 ){
			N = N / 2 ;		// exclude 2 to get odd number
			is_even = true;
		}
	*/

	// check if b is an integer

		var keep_checking = true;

		while ( keep_checking ) {  		// loop, incrementing a.val by 1

			b.val = Math.pow( ( a.val*a.val - N ), 0.5 );   

			if ( b.val % 1 === 0 ){    	// check if int -> stackoverflow.com/a/3886106
				b.is_int = true;		
				keep_checking = false;	// exit loop
			}		

			else
				a.val += 1;
		}

	// once find an integer b

		if (b.is_int){

			var big = {};
			var small = {};

			big.val = a.val + b.val;
				console.log("first factor is " + big.val);
			small.val = a.val - b.val;
				console.log("second factor is " + small.val);

			//could do without, but here it is anyways
			if (big.val == 1 || small.val == 1)
				console.log(N + " is a prime number");

			// check if in array of primes
			if ( first_168.indexOf( big.val ) >= 0 )
				big.is_prime = true;

			if ( first_168.indexOf( small.val ) >= 0 )
				small.is_prime = true;

			// Delete me, just here for the question
			if(big.is_prime)
				console.log("largest prime is " + big.val);
			else if(small.is_prime)
				console.log("largest prime is " + small.val);
		}
}
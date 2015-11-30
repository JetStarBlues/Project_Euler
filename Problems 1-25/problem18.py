nums = [[75],
		[95,64],
		[17,47,82],
		[18,35,87,10],
		[20,4,82,47,65],
		[19,1,23,75,3,34],
		[88,2,77,73,7,63,67],
		[99,65,4,28,6,16,70,92],
		[41,41,26,56,83,40,80,70,33],
		[41,48,72,33,47,32,37,16,94,29],
		[53,71,44,65,25,43,91,52,97,51,14],
		[70,11,33,28,77,73,17,78,39,68,17,57],
		[91,71,52,38,17,14,91,43,58,50,27,29,48],
		[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
		[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

nums2 = [
		[3],
		[4, 7],
		[2, 4, 6],
		[28, 5, 9, 3]]

#=================================================================

####### Trial 1 - assumes largest numbers at bottom ########

# total = nums[0][0]
# cur_idx = 0

# for i in range( 1, len(nums) ):

# 	next_val = max( nums[i][cur_idx], nums[i][cur_idx + 1])

# 	if next_val == nums[i][cur_idx + 1]:
# 		cur_idx = cur_idx + 1

# 	total = total + next_val

# 	print(next_val)

# print("---  ", total)

#=================================================================

#######  Trial 2 - takes forever haha. Logic not very intuitive. Sharability dubious ####### 

# def gen_paths(steps):
# 	ncols = steps #- 1	   	# number of steps in each path
# 	nrows = 2 ** steps  	# number of possible paths

# 	paths = []
# 	for x in range(nrows):
# 		paths.append( [0] * ncols )  	# fill with zeros

# 	odds = list( range(1, nrows, 2) )  	# list of odds

# 	# change every other consecutive group...

# 	for odd in odds:   # makes zero sense without the diagram...lol

# 		for col in range(ncols):

# 			g = 2 ** col   		# length of each group

# 			if g * odd < nrows:

# 				s = g * odd 	# start of every other group

# 				for x in range(g):

# 					# change members of the group to 1 ...
# 					if s + x < nrows:

# 						for _ in range(nrows):

# 							paths[s + x][col] = 1
# 	return paths
# 	# for p in paths:
# 	# 	print (p)

# #print ( gen_paths(6) )

# ####

# def maxSum(list):

# 	sums = []

# 	nrows = len(list)

# 	paths = gen_paths(nrows - 1)  #returns a 2d array

# 	# find sum of a path

# 	for path in paths:

# 		cur_row, cur_col, total = 0, 0, list[0][0]  # initialize

# 		for step in path:

# 			if cur_row < nrows:

# 				cur_row += 1  # increment

# 				if step:
# 					cur_col += 1

# 				#print(cur_row, cur_col)
# 				total += list[cur_row][cur_col]   # add value of selected to total


# 		sums.append(total)

# 	#print(sums)

# 	return max(sums)

# print ( maxSum(nums2) )

#=================================================================

# had to look this one up...
# stackoverflow.com/a/4772727/2354735
#   Has nice graphic illustrating approach
#	 idea is to start from bottom, and tally sum as you move up,
#    deal only w/ 2 levels at a time

# def maxSum(list):

# 	def calc_row_sums (cur):

# 		nxt  = cur + 1

# 		for i in range( len(list[cur]) ):
# 			list[cur][i] += max( list[nxt][i], list[nxt][i+1] )   # replace with sum

# 		del list[nxt]

# 		# print (sums)
# 		# print (list)

	
# 	# move bottom up direction

# 	x = len(list) - 2; # second last row

# 	while x >= 0:
# 		calc_row_sums(x)
# 		x -= 1

# 	return list[0][0]

# print( maxSum(nums) )


#=================================================================

# Further optimizations
# 	no need to del as only returning value

def maxSum(list):

	cur = len(list) - 2; # second last row

	while cur >= 0:

		nxt  = cur + 1

		for i in range( len(list[cur]) ):
			list[cur][i] += max( list[nxt][i], list[nxt][i+1] )   # replace with sum

		cur -= 1

	# print(list)

	return list[0][0]

print( maxSum(nums) )
